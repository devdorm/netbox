import django_tables2 as tables
from netbox.tables import NetBoxTable, ChoiceFieldColumn

from .models import Softwares


class SoftwaresTable(NetBoxTable):
    name = tables.Column(linkify=True)

    class Meta(NetBoxTable.Meta):
        model = Softwares
        fields = ("pk", "id", "name", "actions")
        default_columns = ("name",)
