from django.db.models import Count

from netbox.views import generic
from . import filtersets, forms, models, tables


class testView(generic.ObjectView):
    queryset = models.test.objects.all()


class testListView(generic.ObjectListView):
    queryset = models.test.objects.all()
    table = tables.testTable


class testEditView(generic.ObjectEditView):
    queryset = models.test.objects.all()
    form = forms.testForm


class testDeleteView(generic.ObjectDeleteView):
    queryset = models.test.objects.all()
