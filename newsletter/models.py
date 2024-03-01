from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя пользователя')
    email = models.EmailField(max_length=100, verbose_name='Email')


class Client(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя клиента')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия', **NULLABLE)
    email = models.EmailField(max_length=100, verbose_name='Email')


class LogsForClient(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название рассылки')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    update_at = models.DateTimeField(auto_now=True, verbose_name='дата обновления')
    sent = models.BooleanField(default=False, verbose_name='статус отправки')
    is_active = models.BooleanField(default=True, verbose_name='признак активности')


class Sending(models.Model):
    email = models.EmailField(max_length=100, verbose_name='Email')
    name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия', **NULLABLE)
    message = models.TextField(verbose_name='Сообщение')
