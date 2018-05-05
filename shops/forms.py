from django.forms import ModelForm
from .models import Supply, Delivery


class SupplyForm(ModelForm):
    class Meta:
        model = Supply
        fields = ['supplier', 'weight', 'rate']


class DeliveryForm(ModelForm):
    class Meta:
        model = Delivery
        fields = ['buyer', 'weight', 'rate']