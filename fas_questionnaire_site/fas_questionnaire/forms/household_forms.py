from django import forms
from ..models.household_models import Household


class HouseholdForm(forms.ModelForm):
    class Meta:
        model = Household
        fields = ['village', 'household_number']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

