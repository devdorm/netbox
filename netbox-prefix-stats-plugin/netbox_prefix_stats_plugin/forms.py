from django import forms
from ipam.models import Prefix
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from utilities.forms.fields import CommentField, DynamicModelChoiceField

from .models import prefixstats


class prefixstatsForm(NetBoxModelForm):
    class Meta:
        model = prefixstats
        fields = ("name", "tags")
