from django import forms
from ..models.page11 import *


class LabourDaysEmployedInAgriculturalOperationsForm(forms.ModelForm):

    class Meta:
        model = LabourDaysEmployedInAgriculturalOperations
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}
