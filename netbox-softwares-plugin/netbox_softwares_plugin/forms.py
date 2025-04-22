from netbox.forms import NetBoxModelForm
from .models import Softwares


class Softwares(NetBoxModelForm):
    class Meta:
        model = Softwares
        fields = (
            "device",
            "name",
            "version",
            "source",
            "managed",
            "description",
            "status",
            "install_method",
            "category",
            "install_date",
            "ip_address",
            "port",
            "notes",
        )
