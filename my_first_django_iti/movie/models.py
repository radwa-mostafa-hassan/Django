from django.db import models


class Movie(models.Model):
    name = models.fields.CharField(verbose_name='Movie Name', max_length=50)
    prod_date = models.fields.DateField(verbose_name="Production Date", default='2000-01-01')

    creation_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    actors = models.ManyToManyField('actor.actor')

    def __str__(self):
        return self.name
