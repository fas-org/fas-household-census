from django import forms
from .models import Household, HouseholdIntroduction

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

class HouseholdIntroductionForm(forms.ModelForm):

    class Meta:
        model = HouseholdIntroduction
        fields = ['household', 'household_head_name', 'sex', 'age', 'caste_tribe', 'religion', 'birth_village_tehsil', 'year_of_migration', 'father_name', 'father_occupation', 'address', 'telephone_no']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}