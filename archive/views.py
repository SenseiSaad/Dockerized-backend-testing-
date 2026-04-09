from rest_framework import viewsets, permissions
from .models import ArchiveEntry
from .serializers import ArchiveEntrySerializer

class ArchiveEntryViewSet(viewsets.ModelViewSet):
    serializer_class = ArchiveEntrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Return only the entries belonging to the current user
        return ArchiveEntry.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically set the user to the current authenticated user
        serializer.save(user=self.request.user)
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = User.objects.get(username=response.data['username'])
        refresh = RefreshToken.for_user(user)
        return Response({
            'user': response.data,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
