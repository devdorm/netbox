from netbox.filtersets import NetBoxModelFilterSet
from .models import prefixstats


# class prefixstatsFilterSet(NetBoxModelFilterSet):
#
#     class Meta:
#         model = prefixstats
#         fields = ['name', ]
#
#     def search(self, queryset, name, value):
#         return queryset.filter(description__icontains=value)
