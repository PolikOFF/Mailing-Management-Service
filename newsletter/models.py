from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(models.Model):
    """Модель для пользователя"""
    fio = models.CharField(max_length=150, verbose_name='ФИО пользователя')
    email = models.EmailField(max_length=100, verbose_name='Email')

    def __str__(self):
        return f'Пользователь: {self.fio}, почта: {self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Client(models.Model):
    """Модель клиента"""
    fio = models.CharField(max_length=150, verbose_name='ФИО')
    email = models.EmailField(max_length=100, verbose_name='Email')
    comments = models.TextField(max_length=250, verbose_name="Комментарий")

    def __str__(self):
        return f'Клиент {self.fio}, почта: {self.email}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class LogsForClient(models.Model):
    """Модель для логов"""
    datetime_last_try = models.DateTimeField(verbose_name='дата последней попытки')
    sent_status = models.BooleanField(verbose_name='статус отправки')
    server_response = models.TextField(verbose_name='ответ сервера')

    def __str__(self):
        return f'Ответ сервера - {self.server_response}, статус отправки - {self.sent_status},' \
               f'дата последней попытки {self.datetime_last_try}'

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'


class Sending(models.Model):
    """Модель для настройки рассылки"""
    choices_periodic = [{'once_a_day', 'раз в день'},
                        {'once_a_week', 'раз в неделю'},
                        {'once_a_month', 'раз в месяц'}]

    choices_status = [{'created', 'создана'},
                      {'launched', 'запущена'},
                      {'completed', 'завершена'}]

    mailing_time = models.TimeField(verbose_name="Время рассылки")
    periodicity_mailing = models.IntegerField(choices=choices_periodic, verbose_name='Периодичность рассылки')
    message = models.TextField(verbose_name='Сообщение')
    status_mailing = models.CharField(choices=choices_status, default='created', verbose_name='Статус рассылки')
    message_subject = models.CharField(max_length=150, verbose_name='Тема письма')

    def __str__(self):
        return f"Тема сообщения - {self.message_subject}, статус рассылки - {self.status_mailing}."

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
