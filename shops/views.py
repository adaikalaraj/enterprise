# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, F

from .models import User, Shop, Supplier, Buyer, Supply, Delivery
from .forms import SupplyForm, DeliveryForm

@login_required
def dashboard(request):
	return render(request, "shop/dashboard.html")


@login_required
def supplies(request):
	form = SupplyForm()
	if request.POST:
		form = SupplyForm(request.POST)
		if form.is_valid():
			supply = form.save()
			supply.created_by = request.user
			supply.save()
	supplies = Supply.objects.all()
	total = Supply.objects.aggregate(weight=Sum('weight'), total=Sum(F('weight')*F('rate')))
	return render(request, "shop/supplies.html", {'supplies': supplies, 'total': total, 'form': form})




@login_required
def deliveries(request):
	form = DeliveryForm()
	if request.POST:
		form = DeliveryForm(request.POST)
		if form.is_valid():
			delivery = form.save()
			delivery.created_by = request.user
			delivery.save()
	deliveries = Delivery.objects.all()
	total = Delivery.objects.aggregate(weight=Sum('weight'), total=Sum(F('weight')*F('rate')))
	return render(request, "shop/deliveries.html", {'deliveries': deliveries, 'total': total, 'form': form})


@login_required
def buyers(request):
	buyers = Buyer.objects.all()
	return render(request, "shop/buyers.html", {'buyers': buyers})


@login_required
def suppliers(request):
	suppliers = Supplier.objects.all()
	return render(request, "shop/suppliers.html", {'suppliers': suppliers})
