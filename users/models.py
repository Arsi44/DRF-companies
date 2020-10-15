from django.db import models

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    id = models.AutoField("Id", primary_key=True)
    #username = models.CharField("username", default="None", max_length=50)
    phone = models.CharField("Номер телефона", default="None", max_length=50)
    #first_name = models.CharField("Имя", blank=True, max_length=50)
    #last_name = models.CharField("Фамилия", blank=True, max_length=50)
    #email = models.SlugField('Почта', blank=True, max_length=50)