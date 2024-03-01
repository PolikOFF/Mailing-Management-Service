from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    email = models.EmailField(max_length=200, verbose_name='Email')


class Logs(models.Model):
    pass


class Sending(models.Model):
    email = models.EmailField(max_length=200, verbose_name='Email')
    name = models.CharField(max_length=100, verbose_name='Имя')
