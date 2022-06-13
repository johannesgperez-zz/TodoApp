from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    completed = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['completed']
    
    def __str__(self):
        return self.title
    
