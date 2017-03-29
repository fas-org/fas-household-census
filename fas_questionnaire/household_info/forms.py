from django import forms
from .models import Household, HouseholdMembers


class HouseholdForm(forms.ModelForm):

    class Meta:
        model = Household
        fields = ['Household_number', 'head_name', 'sex', 'age', 'caste', 'religion', 'birth_village', 'year_of_migration', 'father_name', 'father_occupation', 'address', 'telephone']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}


class HouseholdMembersForm(forms.ModelForm):

    class Meta:
        model = HouseholdMembers
        fields = ['Household_number', 'name', 'sex', 'age', 'relationship', 'marital_status', 'occupation', 'place_of_work', 'literacy_status', 'education_level', 'enrolled_institution']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}
