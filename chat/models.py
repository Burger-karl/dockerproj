from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.CharField(max_length=250, unique=True)


# Specify custom related_name for groups and user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Specify a custom related_name
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',  # Specify a custom related_name
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
        )

class ChatHistory(models.Model):  
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    user_chat = models.TextField(null=True, blank=True)
    response_chat = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)