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

    firstName = models.CharField(max_length = 20, default="")

    lastName = models.CharField(max_length = 20, default="")

    def __str__(self):
        return "%s: %s %s" %(self.user, firstName, lastName)

    def __unicode__(self):
        return "%s: %s %s" %(self.user, firstName, lastName)