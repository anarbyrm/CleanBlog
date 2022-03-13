from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=250)
    content = models.TextField()
    author =  models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return self.title