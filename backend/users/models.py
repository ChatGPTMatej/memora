from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLES = (
        ('doctor', 'Doctor'),
        ('relative', 'Relative'),
    )
    role = models.CharField(max_length=20, choices=ROLES)