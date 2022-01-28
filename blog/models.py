from email.policy import default
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='batman.png')

    def __str__(self):
        return f'Perfil de {self.user.username}'

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    timestamp = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=255, default="Hola, soy un post blanco.")
    content = models.TextField()

    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'        

    def __str__(self):
        return f'{self.user.username}: {self.content}'    
