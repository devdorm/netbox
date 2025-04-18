from django import forms
from ipam.models import Prefix
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from utilities.forms.fields import CommentField, DynamicModelChoiceField

from .models import Softwares


class SoftwaresForm(NetBoxModelForm):
    class Meta:
        model = Softwares
        fields = ("name", "tags")
