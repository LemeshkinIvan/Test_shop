from django.db import models


class Subscribers(models.Model):
    class Meta:
        verbose_name = 'subscriber'
        verbose_name_plural = 'subscribers'
    email = models.EmailField('Email')
    name = models.CharField('Name', max_length=20)

    def __str__(self):
        return self.name
