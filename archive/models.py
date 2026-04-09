from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class ArchiveEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='entries', null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    file_attachment = models.FileField(upload_to='archives/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.title}"
    
    class Meta:
        verbose_name_plural = "Archive Entries"
