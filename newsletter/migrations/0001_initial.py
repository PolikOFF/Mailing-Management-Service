# Generated by Django 5.0.2 on 2024-03-13 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=150, verbose_name='ФИО клиента')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('comments', models.TextField(max_length=250, verbose_name='Комментарий')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='LogsForClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_last_try', models.DateTimeField(verbose_name='дата последней попытки')),
                ('sent_status', models.BooleanField(verbose_name='статус отправки')),
                ('server_response', models.TextField(verbose_name='ответ сервера')),
            ],
            options={
                'verbose_name': 'Лог',
                'verbose_name_plural': 'Логи',
            },
        ),
        migrations.CreateModel(
            name='Sending',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mailing_time', models.TimeField(verbose_name='Время рассылки')),
                ('periodicity_mailing', models.IntegerField(choices=[('раз в день', 'once_a_day'), ('once_a_week', 'раз в неделю'), ('once_a_month', 'раз в месяц')], verbose_name='Периодичность рассылки')),
                ('message', models.TextField(verbose_name='Сообщение')),
                ('status_mailing', models.CharField(choices=[('created', 'создана'), ('запущена', 'launched'), ('completed', 'завершена')], default='created', verbose_name='Статус рассылки')),
                ('message_subject', models.CharField(max_length=150, verbose_name='Тема письма')),
            ],
            options={
                'verbose_name': 'Рассылка',
                'verbose_name_plural': 'Рассылки',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=150, verbose_name='ФИО пользователя')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]
