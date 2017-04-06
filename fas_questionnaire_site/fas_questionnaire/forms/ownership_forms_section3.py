from django import forms
from ..models.ownership_models_section3 import AcquisitionMode, IrrigationFlow, IrrigationOwnership, IrrigationSource, CurrentOwnershipHolding


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
