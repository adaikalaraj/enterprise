# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


class Shop(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField(null=True, blank=True)
    amount = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    debt = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)


class Supplier(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='suppliers')
    name = models.CharField(max_length=100)
    joined_date = models.DateField(auto_now_add=True)
    mobile = models.IntegerField(null=True, blank=True)
    amount = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    debt = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)


class Buyer(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='buyers')
    name = models.CharField(max_length=100)
    joined_date = models.DateField(auto_now_add=True)
    mobile = models.IntegerField(null=True, blank=True)
    amount = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    debt = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)


class User(AbstractUser):
    shop = models.ForeignKey(Shop, null=True, blank=True, on_delete=models.CASCADE, related_name='users')
    phone = models.IntegerField(null=True, blank=True)


class Supply(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='supplies')
    date = models.DateField(auto_now_add=True)
    weight = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    rate = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)

    @property
    def amount(self):
        return self.weight * self.rate


class Delivery(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, related_name='deliveries')
    date = models.DateField(auto_now_add=True)
    weight = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    rate = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)

    @property
    def amount(self):
        return self.weight * self.rate
