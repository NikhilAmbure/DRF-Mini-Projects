from django.db import models
from django.contrib.auth.models import User, AbstractUser

class User(AbstractUser):
    email_verified = models.BooleanField(default=False)
    # is_2fa_enbled = models.BooleanField(default=False)