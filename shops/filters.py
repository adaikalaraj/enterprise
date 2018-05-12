import django_filters

from .models import Supply

class SupplyFilter(django_filters.FilterSet):

    class Meta:
        model = Supply
        fields = ['date']