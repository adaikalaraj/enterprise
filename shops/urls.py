from django.conf.urls import url
from django.contrib import admin

from .views import dashboard

urlpatterns = [
    url(r'^$', dashboard, name="dashboard"),
]