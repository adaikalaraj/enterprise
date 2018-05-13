from django.conf.urls import url
from django.contrib import admin

from .views import dashboard, supplies, deliveries, suppliers, buyers, supplier_detail, buyer_detail, delete_supplies, expenses

urlpatterns = [
    url(r'^$', dashboard, name="dashboard"),
    url(r'supplies/$', supplies, name="supplies"),
    url(r'deliveries/$', deliveries, name="deliveries"),
    url(r'buyers/$', buyers, name="buyers"),
    url(r'suppliers/$', suppliers, name="suppliers"),
    url(r'expenses/$', expenses, name="expenses"),
    url(r'suppliers/(?P<pk>\d+)/$', supplier_detail, name="supplier_detail"),
    url(r'buyers/(?P<pk>\d+)/$', buyer_detail, name="buyer_detail"),
    url(r'supplies/delete/(?P<pk>\d+)/$', delete_supplies, name="delete_supplies"),
]