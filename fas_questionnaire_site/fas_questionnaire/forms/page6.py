from django import forms
from ..models.page6 import *


class SalesOfCropProducedForm(forms.ModelForm):
    class Meta:
        model = SalesOfProduction
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}


class ProductionForm(forms.ModelForm):
    class Meta:
        model = Production
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

