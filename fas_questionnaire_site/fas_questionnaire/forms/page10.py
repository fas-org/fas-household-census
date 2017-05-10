from django import forms

from fas_questionnaire.forms.common import ListTextWidget
from fas_questionnaire.models.common import YesOrNo
from ..models.page10 import OtherCosts, OtherCostsItems, PaymentsToManagersAndLongTermWorkers, EmployManagerOrLongTermWorker


class OtherCostsForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput(), required=False)
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

    def __init__(self, *args, **kwargs):
        super(PaymentsToManagersAndLongTermWorkersForm, self).__init__(*args, **kwargs)
        yes_or_no = YesOrNo.objects.values_list('title')
        self.fields['agricultural_labour'].widget = ListTextWidget(data_list=yes_or_no, name='yes_or_no')
        self.fields['operating_agricultural_machinery'].widget = ListTextWidget(data_list=yes_or_no, name='yes_or_no_long_term')
        self.fields['tending_animals'].widget = ListTextWidget(data_list=yes_or_no, name='yes_or_no_long_term')
        self.fields['non_agricultural_businesses'].widget = ListTextWidget(data_list=yes_or_no, name='yes_or_no_long_term')
        self.fields['domestic_work'].widget = ListTextWidget(data_list=yes_or_no, name='yes_or_no_long_term')
        self.fields['activities_others'].widget = ListTextWidget(data_list=yes_or_no, name='yes_or_no_long_term')

class  EmployManagerOrLongTermWorkerForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = EmployManagerOrLongTermWorker
        exclude = ['household']
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        super(EmployManagerOrLongTermWorkerForm, self).__init__(*args, **kwargs)
        yes_or_no = YesOrNo.objects.values_list('title')
        self.fields['employ_manager'].widget = ListTextWidget(data_list=yes_or_no, name='yes_or_no')
        self.fields['employ_long_term_worker'].widget = ListTextWidget(data_list=yes_or_no, name='yes_or_no_long_term')
