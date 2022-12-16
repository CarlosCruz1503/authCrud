from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Task (models.Model):
    name = models.CharField(max_length=50, null=False)
    date_for_complete = models.DateTimeField(null=True)
    important = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    date_complete = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return str(self.name + " usuario : " + str(self.user))
