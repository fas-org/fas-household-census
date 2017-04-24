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


class IncomeFromOtherBusinessActivitiesForm(forms.ModelForm):
    class Meta:
        model = IncomeFromOtherBusinessActivities
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}


class AnimalResoursesInventoryForm(forms.ModelForm):
    class Meta:
        model = AnimalResoursesInventory
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}


class AnimalResourcesFeedForm(forms.ModelForm):
    class Meta:
        model = AnimalResourcesFeed
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}


class OtherExpendituresForm(forms.ModelForm):
    class Meta:
        model = OtherExpenditure
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}
