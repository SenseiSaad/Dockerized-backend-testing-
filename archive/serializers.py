from rest_framework import serializers
from .models import ArchiveEntry

class ArchiveEntrySerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = ArchiveEntry
        fields = ['id', 'user', 'title', 'description', 'file_attachment']
