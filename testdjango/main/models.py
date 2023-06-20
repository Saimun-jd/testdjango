from django.db import models

# Create your models here.
class SocialHandles(models.Model):
    social_id = models.CharField(max_length=100, default='blank')
    social_link=models.CharField(max_length=500, default='blank')
    