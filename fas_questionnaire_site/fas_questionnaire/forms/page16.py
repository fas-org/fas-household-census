from django import forms
from ..models.page16 import *


class IncomeFromStateAndCommonPropertyResourcesForm(forms.ModelForm):
    class Meta:
        model = IncomeFromStateAndCommonPropertyResources
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}


class FreedomOfEmploymentQuestionsForm(forms.ModelForm):
    class Meta:
        model = FreedomOfEmploymentQuestions
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}


class AgriculturalOrNonAgriculturalLabourServicesForm(forms.ModelForm):
    class Meta:
        model = AgriculturalOrNonAgriculturalLabourServices
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}
