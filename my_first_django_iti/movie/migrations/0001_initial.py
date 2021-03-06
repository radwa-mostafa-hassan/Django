# Generated by Django 2.2.12 on 2022-06-05 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('actor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Movie Name')),
                ('prod_date', models.DateField(default='2000-01-01', verbose_name='Production Date')),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('actors', models.ManyToManyField(to='actor.Actor')),
            ],
        ),
    ]
