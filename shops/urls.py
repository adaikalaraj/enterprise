from django.conf.urls import url
from django.contrib import admin

from .views import dashboard, supplies, deliveries, suppliers, buyers

urlpatterns = [
    url(r'^$', dashboard, name="dashboard"),
    url(r'supplies/$', supplies, name="supplies"),
    url(r'deliveries/$', deliveries, name="deliveries"),
    url(r'buyers/$', buyers, name="buyers"),
    url(r'suppliers/$', suppliers, name="suppliers"),
]