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
        model=IncomeFromOtherBusinessActivities
        exclude=['household']
        widgets=None
        localized_fields=None
        labels={
            'rents_paid':'Rents Paid(for land,building or machine)',
            'rents_paid':'Any other costs(specify)'
        }
        help_texts={}
        error_messages={}
