from netbox.forms import NetBoxModelForm
from .models import InstalledSoftware


class InstalledSoftwareForm(NetBoxModelForm):
    class Meta:
        model = InstalledSoftware
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
