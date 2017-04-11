from django import forms
from ..models.othercosts import OtherCosts
from ..models.othercosts import OtherCostsItems


class OtherCostsForm(forms.ModelForm):
    class Meta:
        model = OtherCosts
        exclude = ['household', 'record_type']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}


class OtherCostsExtraForm(forms.ModelForm):
    class Meta:
        model = OtherCosts
        exclude = ['household', 'record_type']
        widgets = {
            'item': forms.Select(choices=[ (c.item,c.item) for c in OtherCostsItems.objects.all()])
        }
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}
