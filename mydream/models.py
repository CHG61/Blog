from django.db import models

class Dream(models.Model):
    title = models.CharField(max_length=2000)
    description = models.TextField()
    image = models.ImageField(upload_to='dreams/', blank=True, null=True)
    video = models.FileField(upload_to='dreams/', blank=True, null=True)  # video alanı

    def __str__(self):
        return self.title
