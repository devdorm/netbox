from netbox.filtersets import NetBoxModelFilterSet
from .models import Softwares


# class SoftwaresFilterSet(NetBoxModelFilterSet):
#
#     class Meta:
#         model = Softwares
#         fields = ['name', ]
#
#     def search(self, queryset, name, value):
#         return queryset.filter(description__icontains=value)
