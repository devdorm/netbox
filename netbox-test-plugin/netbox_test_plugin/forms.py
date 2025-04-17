from django import forms
from ipam.models import Prefix
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from utilities.forms.fields import CommentField, DynamicModelChoiceField

from .models import test


class testForm(NetBoxModelForm):
    class Meta:
        model = test
        fields = ("name", "tags")
