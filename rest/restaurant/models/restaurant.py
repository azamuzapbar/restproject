from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Restaurant(models.Model):
    name = models.CharField(verbose_name='название', max_length=100)
    address = models.CharField(verbose_name='адрес', max_length=200)
    description = models.TextField(verbose_name='описание', max_length=2000)
    phone = PhoneNumberField(null=False, blank=False, unique=True)

    def __str__(self):
        return self.name
