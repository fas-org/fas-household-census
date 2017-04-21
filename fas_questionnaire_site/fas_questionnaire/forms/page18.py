from django import forms
from ..models.page18 import *


class AcquisitionAndLossOfMajorAssetsForm(forms.ModelForm):
    class Meta:
        model = AcquisitionAndLossOfMajorAssets
        exclude = ['household']
        widgets = None
        localized_fields = None
        help_texts = {}
        error_messages = {}
