from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractBaseUser):
    first_name = models.CharField(verbose_name='Имя', null=True, blank=True, max_length=250)
    last_name = models.CharField(verbose_name='Фамилия', null=True, blank=True, max_length=250)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)
    username = models.CharField(verbose_name='Логин', max_length=250, blank=False, null=False)
    email = models.EmailField(verbose_name='почта', null=False, blank=False)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)