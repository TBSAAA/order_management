import random
from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from utils.encrypt import md5
from web import models
from django_redis import get_redis_connection

class LoginForm(forms.Form):
    telephone = forms.CharField(max_length=11, min_length=11, validators=[RegexValidator(r'1[3-9]\d{9}', message='手机号码格式错误')])
    password = forms.CharField(max_length=32, min_length=6, error_messages={'max_length': '密码最多不能超过32位', 'min_length': '密码最少不能少于6位'})
    remember = forms.IntegerField(required=False)

    def clean(self):
        cleaned_data = super().clean()
        telephone = cleaned_data.get('telephone')
        password = cleaned_data.get('password')
        user = models.User.objects.filter(telephone=telephone).first()
        if not user:
            raise ValidationError('手机号码或者密码错误')
        if not user.check_password(password):
            raise ValidationError('手机号码或者密码错误')
        cleaned_data['user'] = user
        return cleaned_data