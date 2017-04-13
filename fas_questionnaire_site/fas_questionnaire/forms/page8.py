from django import forms
from ..models.page8 import *


class ExtensionForm(forms.ModelForm):

    class Meta:
        model = Extension
        fields = ['household', 'from_whom_advice_received', 'type_of_advice_received_description']
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {
            'from_whom_advice_received': 'Did you receive any advice regarding cultivation of crops during the last year',
            'type_of_advice_received_description': 'If Yes, what kind of advice did you receive?'
        }
        help_texts = {}
        error_messages = {}


class InstitutionalSupportForm(forms.ModelForm):

    class Meta:
        model = InstitutionalSupport
        fields = ['household', 'category', 'name_of_institution', 'year_of_support','nature_of_support_or_purpose', 'comments']
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}


class InstitutionalSupportCommentsForm(forms.ModelForm):

    class Meta:
        model = InstitutionalSupportComments
        fields = ['household', 'institutional_support_comments']
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {
            'institutional_support_comments': 'Comments/ Notes'
        }
        help_texts = {}
        error_messages = {}