# models.py
from django.db import models

class WorkExperience(models.Model):
    CATEGORY_CHOICES = [
        ('worklife', 'Work Life'),
        ('cv', 'My CV'),
        ('dataanalyst', 'Data Analyst'),
    ]

    title = models.CharField(max_length=2000)
    content = models.TextField()
    image = models.ImageField(upload_to='work_images/', blank=True, null=True)
    video = models.FileField(upload_to='work_videos/', blank=True, null=True)

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='worklife')

    def __str__(self):
        return f"{self.title} ({self.get_category_display()})"
