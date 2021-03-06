# Generated by Django 2.2.3 on 2019-07-05 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ForecastApp', '0003_forecast_rain'),
    ]

    operations = [
        migrations.AddField(
            model_name='forecast',
            name='clodly',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='forecast',
            name='more_sunny',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='forecast',
            name='snow',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='forecast',
            name='thunder',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='forecast',
            name='week_day',
            field=models.CharField(default='Monday', max_length=200),
        ),
    ]
