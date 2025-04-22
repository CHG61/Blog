from django.db import models

class HomepageHighlight(models.Model):
    title = models.CharField(max_length=2000)
    content = models.TextField()
    image = models.ImageField(upload_to='homepage/', blank=True, null=True)
    video = models.FileField(upload_to='homepage/', blank=True, null=True)

    def __str__(self):
        return self.title
