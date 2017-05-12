from django import forms

from fas_questionnaire.forms.common import ListTextWidget
from ..models.page2 import *
from ..views.common import is_empty


class AcquisitionModeForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = AcquisitionMode
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}


class IrrigationFlowForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = IrrigationFlow
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}


class IrrigationOwnershipForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = IrrigationOwnership
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}


class IrrigationSourceForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = IrrigationSource
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}


class CurrentOwnershipHoldingForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = CurrentOwnershipHolding
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        super(CurrentOwnershipHoldingForm, self).__init__(*args, **kwargs)
        land_type_list = LandType.objects.values_list('type')
        self.fields['land_type'].widget = ListTextWidget(data_list=land_type_list, name='land_type-list')
        acquisition_mode_list = AcquisitionMode.objects.values_list('acquisition')
        self.fields['acquisition_mode'].widget = ListTextWidget(data_list=acquisition_mode_list, name='acquisition_mode-list')
        irrigation_source_list = IrrigationSource.objects.values_list('source')
        self.fields['irrigation_source'].widget = ListTextWidget(data_list=irrigation_source_list, name='irrigation_source-list')
        irrigation_flow_list = IrrigationFlow.objects.values_list('type')
        self.fields['irrigation_flow'].widget = ListTextWidget(data_list=irrigation_flow_list, name='irrigation_flow-list')
        irrigation_ownership_list = IrrigationOwnership.objects.values_list('owner')
        self.fields['irrigation_ownership'].widget = ListTextWidget(data_list=irrigation_ownership_list, name='irrigation_ownership-list')

    def clean(self):
        for param in self.cleaned_data:
            if not param == 'land_type' and not is_empty(self.cleaned_data[param]):
                if self.cleaned_data['land_type'] is None:
                    raise forms.ValidationError('Land Type is mandatory for entering other details in the record')
        return self.cleaned_data


class HomesteadAreaForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = HomesteadArea
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def clean(self):
        print(self.cleaned_data)
        if self.cleaned_data.get('id') is None and \
                (self.cleaned_data.get('components') is None or self.cleaned_data.get('area') is None):
            raise forms.ValidationError('Both Component and Area need to be entered')
        if self.cleaned_data.get('id') is not None and \
                (self.cleaned_data.get('components') is None and self.cleaned_data.get('area') is not None) or \
                (self.cleaned_data.get('components') is not None and self.cleaned_data.get('area') is None):
            raise forms.ValidationError('Both Component and Area need to be entered')
        return self.cleaned_data

    def __init__(self, *args, **kwargs):
        super(HomesteadAreaForm, self).__init__(*args, **kwargs)
        components_list = HomesteadComponents.objects.values_list('components')
        self.fields['components'].widget = ListTextWidget(data_list=components_list, name='components-list')


class LandPurchasedForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = LandPurchased
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        super(LandPurchasedForm, self).__init__(*args, **kwargs)
        type_of_land_purchased_list = LandType.objects.values_list('type')
        self.fields['type_of_land_purchased'].widget = ListTextWidget(data_list=type_of_land_purchased_list, name='type_of_land_purchased-list')
        caste_of_seller_list = Caste.objects.values_list('caste')
        self.fields['caste_of_seller'].widget = ListTextWidget(data_list=caste_of_seller_list, name='caste_of_seller-list')
        occupation_of_seller_list = Occupation.objects.values_list('occupation')
        self.fields['occupation_of_seller'].widget = ListTextWidget(data_list=occupation_of_seller_list,
                                                                 name='occupation_of_seller-list')



class LandSoldForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = LandSold
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        super(LandSoldForm, self).__init__(*args, **kwargs)
        type_of_land_sold_list = LandType.objects.values_list('type')
        self.fields['type_of_land_sold'].widget = ListTextWidget(data_list=type_of_land_sold_list, name='type_of_land_sold-list')
        caste_of_buyer_list = Caste.objects.values_list('caste')
        self.fields['caste_of_buyer'].widget = ListTextWidget(data_list=caste_of_buyer_list, name='caste_of_buyer-list')
        occupation_of_buyer_list = Occupation.objects.values_list('occupation')
        self.fields['occupation_of_buyer'].widget = ListTextWidget(data_list=occupation_of_buyer_list,
                                                                 name='occupation_of_buyer-list')



