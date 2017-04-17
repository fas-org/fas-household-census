from django import forms
from ..models.page_13 import PatternOfAgriculturalLabouringOut
from ..models.common import Crop
from ..models.householdmembers import HouseholdMembers


class PatternOfAgriculturalLabouringOutForm(forms.ModelForm):
    """Pattern of Agricultural Labouring Out Form"""
    class Meta:
        model = PatternOfAgriculturalLabouringOut
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}
