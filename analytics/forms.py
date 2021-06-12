from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, help_text='Required. 100 charaters of fewer.')
    last_name = forms.CharField(max_length=100, help_text='Required. 100 charaters of fewer.')

    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name')
