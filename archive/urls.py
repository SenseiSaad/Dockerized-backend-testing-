from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArchiveEntryViewSet

router = DefaultRouter()
router.register(r'entries', ArchiveEntryViewSet, basename='archiveentry')

urlpatterns = [
    path('', include(router.urls)),
]
