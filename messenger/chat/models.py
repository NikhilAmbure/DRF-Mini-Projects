from django.db import models
from django.contrib.auth.models import User


class Messages(models.Model):
    message = models.TextField()