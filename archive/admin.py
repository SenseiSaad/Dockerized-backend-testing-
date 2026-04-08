from django.contrib import admin
from .models import ArchiveEntry

@admin.register(ArchiveEntry)
class ArchiveEntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'file_attachment')
