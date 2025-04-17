from netbox.filtersets import NetBoxModelFilterSet
from .models import test


# class testFilterSet(NetBoxModelFilterSet):
#
#     class Meta:
#         model = test
#         fields = ['name', ]
#
#     def search(self, queryset, name, value):
#         return queryset.filter(description__icontains=value)
