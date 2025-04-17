from django.db.models import Count

from netbox.views import generic
from . import filtersets, forms, models, tables


class prefixstatsView(generic.ObjectView):
    queryset = models.prefixstats.objects.all()


class prefixstatsListView(generic.ObjectListView):
    queryset = models.prefixstats.objects.all()
    table = tables.prefixstatsTable


class prefixstatsEditView(generic.ObjectEditView):
    queryset = models.prefixstats.objects.all()
    form = forms.prefixstatsForm


class prefixstatsDeleteView(generic.ObjectDeleteView):
    queryset = models.prefixstats.objects.all()
