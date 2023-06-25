from django.db import models
from django.utils.translation import gettext_lazy as _

class Page(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=30)
    content = models.TextField()

class Country(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('Имя'))
    alias = models.CharField(max_length=30)

    def __str__(self):
        return self.name 

class City(models.Model):
    name = models.CharField(max_length=50)
    alias = models.CharField(max_length=30)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
