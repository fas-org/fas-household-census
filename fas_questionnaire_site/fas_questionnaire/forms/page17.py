from django import forms
from ..models.page17 import *


class IncomeFromSalariesForm(forms.ModelForm):
    class Meta:
        model = IncomeFromSalaries
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}
