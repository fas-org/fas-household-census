from django import forms
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
        if self.cleaned_data.get('components') is None or self.cleaned_data.get('area') is None:
            raise forms.ValidationError('Both Component and Area need to be entered')
        return self.cleaned_data


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


class LandPurchasedCommentsForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = LandPurchasedComments
        fields = ['household', 'landpurchased_comments','id']
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}
