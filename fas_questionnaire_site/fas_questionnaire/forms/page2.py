from django import forms
from ..models.page2 import *


class AcquisitionModeForm(forms.ModelForm):

    class Meta:
        model = AcquisitionMode
        fields = ['acquisition']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}


class IrrigationFlowForm(forms.ModelForm):

    class Meta:
        model = IrrigationFlow
        fields = ['type']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}


class IrrigationOwnershipForm(forms.ModelForm):

    class Meta:
        model = IrrigationOwnership
        fields = ['owner']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}


class IrrigationSourceForm(forms.ModelForm):

    class Meta:
        model = IrrigationSource
        fields = ['source']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}


class CurrentOwnershipHoldingForm(forms.ModelForm):

    class Meta:
        model = CurrentOwnershipHolding
        fields = ['household', 'ownership_plot_no', 'land_type', 'extent_owned_land', 'acquisition_mode', 'irrigation_source', 'irrigation_flow', 'irrigation_ownership', 'value', 'comments']
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def clean(self):
        if self.cleaned_data.get('land_type') is None:
            raise forms.ValidationError('Land Type is mandatory for entering other details in the record')
        return self.cleaned_data


class HomesteadAreaForm(forms.ModelForm):

    class Meta:
        model = HomesteadArea
        fields = ['household', 'components', 'area']
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
    class Meta:
        model = LandPurchased
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}


class LandSoldForm(forms.ModelForm):
    class Meta:
        model = LandSold
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}


class LandPurchasedCommentsForm(forms.ModelForm):
    class Meta:
        model = LandPurchasedComments
        fields = ['household', 'landpurchased_comments']
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}
