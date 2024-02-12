from django.db import models

class VideoFile(models.Model):
    file_name = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file_url = models.URLField(max_length=1024)
