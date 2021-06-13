from .models import House
import django_filters


class HouseFilter(django_filters.FilterSet):
    # name = django_filters.CharFilter(label='Поиск', lookup_expr='icontains')

    class Meta:
        model = House
        # fields = ['name', 'house_class', 'status', 'availability_of_apartments', 'developer']
        fields = ['house_class', 'status', 'availability_of_apartments', 'developer']
