# Generated by Django 2.2.12 on 2022-06-08 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='age',
            field=models.DateField(default='2000-01-01', verbose_name='Actor Age'),
        ),
    ]
