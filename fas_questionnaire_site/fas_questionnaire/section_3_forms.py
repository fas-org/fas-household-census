from django import forms
from .section_3_models import AcquisitionMode, IrrigationFlow, IrrigationOwnership, IrrigationSource, Land, CurrentOwnershipHolding


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


class LandForm(forms.ModelForm):

    class Meta:
        model = Land
        fields = ['land_type']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}


class CurrentOwnershipHoldingForm(forms.ModelForm):

    class Meta:
        model = CurrentOwnershipHolding
        fields = ['household', 'land_type', 'extent_owned_land', 'acquisition_mode', 'irrigation_source', 'irrigation_flow', 'irrigation_ownership', 'value']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}
