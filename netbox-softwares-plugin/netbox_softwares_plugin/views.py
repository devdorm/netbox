from django.db.models import Count

from netbox.views import generic
from . import filtersets, forms, models, tables


class SoftwaresView(generic.ObjectView):
    queryset = models.Softwares.objects.all()


class SoftwaresListView(generic.ObjectListView):
    queryset = models.Softwares.objects.all()
    table = tables.SoftwaresTable


class SoftwaresEditView(generic.ObjectEditView):
    queryset = models.Softwares.objects.all()
    form = forms.SoftwaresForm


class SoftwaresDeleteView(generic.ObjectDeleteView):
    queryset = models.Softwares.objects.all()
