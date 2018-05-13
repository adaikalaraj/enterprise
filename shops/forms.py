from django.forms import ModelForm
from .models import Supply, Delivery, Expense


class SupplyForm(ModelForm):
    class Meta:
        model = Supply
        fields = ['supplier', 'buyer', 'weight', 'rate', 'debt']


class DeliveryForm(ModelForm):
    class Meta:
        model = Delivery
        fields = ['buyer', 'credit']


class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = ['employee', 'amount', 'reason']
