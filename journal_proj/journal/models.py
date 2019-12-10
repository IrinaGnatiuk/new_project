from django.db import models
import datetime
from django.utils import timezone


class Users(models.Model):
    login = models.CharField( max_length=250, unique=True)
    password = models.CharField(max_length=250)

    def __str__(self):
        return self.login


class Trade(models.Model):
    login = models.ForeignKey(Users, on_delete=models.CASCADE)
    secur_name = models.CharField(max_length=250)
    price_open = models.DecimalField(max_digits=8, decimal_places=2)
    quantity_open = models.IntegerField(default=0)
    date = models.DateTimeField('date open')


class Trade_close(models.Model):
    open_trade = models.ForeignKey(Trade, on_delete=models.CASCADE)
    price_close = models.DecimalField(max_digits=8, decimal_places=2)
    quantity_close = models.IntegerField(default=0)
    date = models.DateTimeField('date close')
