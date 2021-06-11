from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser


# class SignupForm(models.Model):
#     username = models.CharField(max_length=50)
#     firstname = models.CharField(max_length=50)
#     lastname = models.CharField(max_length=50)
#     email = models.EmailField()
#     password = forms.CharField(widget=forms.PasswordInput())
#
#
# class LoginForm(models.Model):
#     username = models.CharField(max_length=50)
#     password = forms.CharField(widget=forms.PasswordInput())


class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=100, blank=False)
    age = models.PositiveIntegerField(null=True, blank=True)
