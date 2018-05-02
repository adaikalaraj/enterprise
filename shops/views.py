# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import User


@login_required
def dashboard(request):
	return render(request, "shop/dashboard.html")
