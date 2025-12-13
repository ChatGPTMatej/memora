from django.db import models
from users.models import User

class Person(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='persons')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    photo = models.ImageField(upload_to='faces/', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"