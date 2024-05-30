# Create your models here.
# This model is for users, when they input their information, this model allows them to create a new user
# account in Django Admin
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(null=True)
    bio = models.CharField(max_length=140, blank=True)
    phone_number = models.CharField(max_length=12, blank=True)

    # To let the Profile page show 'user's Profile' in admin profile page
    def __str__(self):
        return f'{self.user.username}\'s Profile'