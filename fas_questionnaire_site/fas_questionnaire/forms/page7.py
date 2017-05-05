from django import forms
from ..models.page7 import InputUseSeeds, InputUseFertiliser, InputUseManure, InputUsePlantProtection, InputUseIrrigation

class InputUseManureForm(forms.ModelForm):
    class Meta:
        model = InputUseManure
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}


class InputUsePlantProtectionForm(forms.ModelForm):
    class Meta:
        model = InputUsePlantProtection
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}


class InputUseIrrigationForm(forms.ModelForm):
    class Meta:
        model = InputUseIrrigation
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}


class InputUseFertiliserForm(forms.ModelForm):
    class Meta:
        model = InputUseFertiliser
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}


class InputUseSeedsForm(forms.ModelForm):
    class Meta:
        model = InputUseSeeds
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}
