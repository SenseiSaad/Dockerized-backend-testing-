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