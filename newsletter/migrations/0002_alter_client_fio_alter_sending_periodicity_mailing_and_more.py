# Generated by Django 5.0.2 on 2024-03-13 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='fio',
            field=models.CharField(max_length=150, verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='sending',
            name='periodicity_mailing',
            field=models.IntegerField(choices=[('раз в день', 'once_a_day'), ('раз в неделю', 'once_a_week'), ('once_a_month', 'раз в месяц')], verbose_name='Периодичность рассылки'),
        ),
        migrations.AlterField(
            model_name='sending',
            name='status_mailing',
            field=models.CharField(choices=[('создана', 'created'), ('запущена', 'launched'), ('completed', 'завершена')], default='created', verbose_name='Статус рассылки'),
        ),
    ]
