from django.db import models
from users.models import User

class Person(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='persons')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    relationship = models.CharField(max_length=50)
    last_visit_date = models.DateField(null=True, blank=True)
    last_visit_reason = models.TextField(blank=True)
    last_conversation = models.TextField(blank=True)
    photo = models.ImageField(upload_to='faces/')