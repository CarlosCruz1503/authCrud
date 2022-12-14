from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True,blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title