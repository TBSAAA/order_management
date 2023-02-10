import random
from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from utils.encrypt import md5
from web import models
from django_redis import get_redis_connection


class RegisterForm(forms.Form):
    username = forms.CharField(
        validators=[
            RegexValidator(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', 'please input email address'), ],
        widget=forms.TextInput(attrs={"class": "no-border", "placeholder": "email"}),
    )

    password = forms.CharField(
        min_length=8,
        max_length=32,
        widget=forms.PasswordInput(attrs={"class": "no-border", "placeholder": "password"}, render_value=True)
    )

    password_repeat = forms.CharField(
        min_length=8,
        max_length=32,
        widget=forms.PasswordInput(attrs={"class": "no-border", "placeholder": "password again"}, render_value=True)
    )

    def clean_password_repeat(self):
        password = self.cleaned_data.get('password')
        password_repeat = self.cleaned_data.get('password_repeat')
        if password == password_repeat:
            return md5(password_repeat)
        else:
            raise ValidationError('password is not the same')
