# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


class Shop(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField(null=True, blank=True)
    amount = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    debt = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)

    def __str__(self):
        return self.name


class Supplier(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='suppliers')
    name = models.CharField(max_length=100)
    joined_date = models.DateField(auto_now_add=True)
    mobile = models.IntegerField(null=True, blank=True)
    amount = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    debt = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)

    def __str__(self):
        return self.name


class Buyer(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='buyers')
    name = models.CharField(max_length=100)
    joined_date = models.DateField(auto_now_add=True)
    mobile = models.IntegerField(null=True, blank=True)
    amount = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    debt = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)

    def __str__(self):
        return self.name


class User(AbstractUser):
    shop = models.ForeignKey(Shop, null=True, blank=True, on_delete=models.CASCADE, related_name='users')
    phone = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.username


class Supply(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='supplies')
    date = models.DateField(auto_now_add=True)
    weight = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    rate = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    created_by = models.ForeignKey(User, null=True, blank=True, related_name='supplies')

    @property
    def amount(self):
        return round(self.weight * self.rate, 2)


    def __str__(self):
        return '{} {}'.format(self.supplier, self.date)


class Delivery(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, related_name='deliveries')
    date = models.DateField(auto_now_add=True)
    weight = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    rate = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    created_by = models.ForeignKey(User, null=True, blank=True, related_name='deliveries')

    @property
    def amount(self):
        return self.weight * self.rate

    def __str__(self):
        return '{} {}'.format(self.buyer, self.date)
