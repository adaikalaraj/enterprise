# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Shop, Supplier, Buyer, User, Supply, Delivery


admin.site.register(Shop)
admin.site.register(Supplier)
admin.site.register(Buyer)
admin.site.register(User)
admin.site.register(Supply)
admin.site.register(Delivery)