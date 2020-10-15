from django_filters import rest_framework as filters
from .models import Product

# ссылка на документацию
# https://django-filter.readthedocs.io/en/latest/guide/tips.html


# наследуемся от BaseInFilter, чтобы использовать lookup_expr далее
class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class ProductFilter(filters.FilterSet):
    company = CharFilterInFilter(field_name='company__title_com', lookup_expr='in')
    categories = CharFilterInFilter(field_name='category__title_cat', lookup_expr='in')
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['company', 'categories', 'title']
