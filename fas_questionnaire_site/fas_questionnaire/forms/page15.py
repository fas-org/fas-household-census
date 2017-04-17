from django import forms
from ..models.page15 import *


class LongTermWorkersForm(forms.ModelForm):
    class Meta:
        model = LongTermWorkers
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}


class NonAgricultureWorkersForm(forms.ModelForm):
    class Meta:
        model = NonAgricultureWorkers
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}
