from django.db import models
from django.contrib.auth.models import User
from achievement.models import Achievement

# Create your models here.
GENDER_CHOICES = (
    ("M", "Male"), 
    ("F", "Female")
)

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    gender = models.CharField(max_length = 1, choices = GENDER_CHOICES)

    def __str__(self):
        return "%s" %self.user

    def __unicode__(self):
        return "%s" %self.user