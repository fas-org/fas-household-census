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
        widgets = {}
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        """Initialize the choices for item widget"""
        super(OtherCostsExtraForm, self).__init__(*args, **kwargs)
        self.fields['item'].widget = forms.Select(choices=[ (c.item, c.item) for c in OtherCostsItems.objects.all()])
