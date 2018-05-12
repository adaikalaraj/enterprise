# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, F

from django.utils import timezone

from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import User, Shop, Supplier, Buyer, Supply, Delivery
from django.contrib.auth.decorators import user_passes_test
from .forms import SupplyForm, DeliveryForm
from .filters import SupplyFilter

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
			supplier = supply.supplier
			supplier.amount = float(supplier.amount) + supply.final_amount - float(supply.debt)
			supplier.save()
			delivery = Delivery.objects.create(buyer=supply.buyer, weight=supply.weight, rate=supply.rate, created_by=supply.created_by)
			supply.delivery = delivery
			supply.save()
			buyer = supply.buyer
			buyer.amount = float(buyer.amount) - float(delivery.amount)
			buyer.save()

	supplies = Supply.objects.filter(date=timezone.now())
	total = supplies.aggregate(weight=Sum('weight'), total=Sum(F('weight')*F('rate')))
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
			buyer = delivery.buyer
			buyer.amount = float(buyer.amount) + float(delivery.credit)
			buyer.save()
	deliveries = Delivery.objects.filter(date=timezone.now())
	total = deliveries.aggregate(weight=Sum('weight'), total=Sum(F('weight')*F('rate')))
	return render(request, "shop/deliveries.html", {'deliveries': deliveries, 'total': total, 'form': form,})


@login_required
def buyers(request):
	buyers = Buyer.objects.all()
	return render(request, "shop/buyers.html", {'buyers': buyers})


@login_required
def suppliers(request):
	suppliers = Supplier.objects.all()
	return render(request, "shop/suppliers.html", {'suppliers': suppliers})


@login_required
def supplier_detail(request, pk):
	supplier = Supplier.objects.get(id=pk)
	date = request.GET.get('date')
	supplies = Supply.objects.filter(supplier=supplier).order_by('date')
	if date:
		date = date.split('-')
		month = date[0]
		year = date[1]
		supplies = Supply.objects.filter(supplier=supplier, date__month=month, date__year=year).order_by('date')
	total = supplies.aggregate(weight=Sum('weight'), total=Sum(F('weight')*F('rate')))
	total_amount = 0.0
	if total.get('total') != None:
		total_amount = total.get('total')
	print total_amount
	commission = round((total_amount /10), 2)
	final_amount = float(total_amount) - float(commission)
	return render(request, "shop/supplier_detail.html", {'supplier': supplier, 'supplies': supplies, 'total': total, 'final_amount':final_amount,'commission':commission})



@login_required
def buyer_detail(request, pk):
	buyer = Buyer.objects.get(id=pk)
	date = request.GET.get('date')
	deliveries = Delivery.objects.filter(buyer=buyer).order_by('date')
	if date:
		date = date.split('-')
		month = date[0]
		year = date[1]
		deliveries = Delivery.objects.filter(buyer=buyer, date__month=month, date__year=year).order_by('date')
	total = deliveries.aggregate(weight=Sum('weight'), total=Sum(F('weight')*F('rate')))
	return render(request, "shop/buyer_detail.html", {'buyer': buyer, 'deliveries': deliveries, 'total': total,})


@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_supplies(request, pk):
	supply = Supply.objects.get(id=pk)
	delivery = supply.delivery
	supply.supplier.amount = float(supply.supplier.amount) - supply.final_amount + float(supply.debt)
	delivery.buyer.amount = float(delivery.buyer.amount) + float(delivery.amount)
	supply.supplier.save()
	delivery.buyer.save()
	supply.delete()
	delivery.delete()
	return HttpResponseRedirect(reverse('supplies'))
