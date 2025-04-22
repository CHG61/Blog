from django.db import models

class Education(models.Model):
    CATEGORY_CHOICES = [
        ('general', 'General'),
        ('erasmus', 'Erasmus+'),
        ('university', 'University'),
        ('data', 'Data'),
        ('sports', 'Sports'),
    ]
    title = models.CharField(max_length=2000)
    content = models.TextField()
    image = models.ImageField(upload_to='education_images/', blank=True, null=True)
    video = models.FileField(upload_to='education/videos/', blank=True, null=True)

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='general')

    def __str__(self):
        return f"{self.title} ({self.get_category_display()})"
