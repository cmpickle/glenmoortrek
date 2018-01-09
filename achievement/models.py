from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Achievement(models.Model):
    title = models.CharField(max_length=50)

    image = models.ImageField(upload_to='achievemnt_images')

    description = models.CharField(max_length=250)

    users = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.title