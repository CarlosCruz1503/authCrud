from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Group (models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    phone = models.CharField(default="0", blank=False,
                             null=False, max_length=13)
    email = models.EmailField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)
    favorite = models.BooleanField(default=False)
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, blank=True, null =True, )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name + " usuario : " + str(self.user))
