from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel
from dcim.models import Device


class Softwares(NetBoxModel):
    SOURCE_CHOICES = [
        ("agent", "Agent"),
        ("manual", "Manual"),
        ("api", "API"),
        ("other", "Other"),
    ]

    STATUS_CHOICES = [
        ("running", "Running"),
        ("stopped", "Stopped"),
        ("unknown", "Unknown"),
    ]

    INSTALL_METHOD_CHOICES = [
        ("apt", "APT"),
        ("rpm", "RPM"),
        ("source", "Source"),
        ("container", "Container"),
        ("other", "Other"),
    ]

    CATEGORY_CHOICES = [
        ("webserver", "Web Server"),
        ("database", "Database"),
        ("monitoring", "Monitoring"),
        ("other", "Other"),
    ]

    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name="installed_softwares")
    name = models.CharField(max_length=100)
    version = models.CharField(max_length=50)
    source = models.CharField(max_length=20, choices=SOURCE_CHOICES)
    managed = models.BooleanField(default=True)

    description = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, blank=True)
    install_method = models.CharField(max_length=20, choices=INSTALL_METHOD_CHOICES, blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, blank=True)
    install_date = models.DateField(blank=True, null=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    port = models.PositiveIntegerField(blank=True, null=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} on {self.device.name} ({self.version})"

    def get_absolute_url(self):
        return reverse("plugins:netbox_softwares_plugin:softwares", args=[self.pk])
