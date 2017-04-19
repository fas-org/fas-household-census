from django import forms
from ..models.page10 import OtherCosts, OtherCostsItems, PaymentsToManagersAndLongTermWorkers, EmployManagerOrLongTermWorker


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

class PaymentsToManagersAndLongTermWorkersForm(forms.ModelForm):
    class Meta:
        model = PaymentsToManagersAndLongTermWorkers
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}


class  EmployManagerOrLongTermWorkerForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = EmployManagerOrLongTermWorker
        exclude = ['household']
        widgets = {}
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}