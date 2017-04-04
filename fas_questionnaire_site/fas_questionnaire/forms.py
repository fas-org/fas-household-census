from django import forms
from .models import Household, HouseholdIntroduction, LandBought, LandSold


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
        fields = ['household', 'household_head_name', 'sex', 'age', 'caste_tribe', 'religion', 'birth_village_tehsil',
                  'year_of_migration', 'father_name', 'father_occupation', 'address', 'telephone_no']
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}


class LandBoughtForm(forms.ModelForm):
    class Meta:
        model = LandBought
        fields = ['year_of_purchase', 'extent', 'type_of_land', 'seller', 'price_of_land', 'comments']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}


class LandSoldForm(forms.ModelForm):
    class Meta:
        model = LandSold
        fields = ['year_of_sale', 'extent', 'type_of_land', 'buyer', 'price_of_land', 'reasons_for_sale']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}
