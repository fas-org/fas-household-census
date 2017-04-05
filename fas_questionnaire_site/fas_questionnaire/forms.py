from django import forms
from .models import Household, HouseholdIntroduction, LandBought, LandSold, Buyer, Seller


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

    # this is to remove the mandatory fields
    def __init__(self, *args, **kwargs):
        super(HouseholdIntroductionForm, self).__init__(*args, **kwargs)
        for key in self.fields:
            self.fields[key].required = False


class BuyerForm(forms.ModelForm):
    class Meta:
        model = Buyer
        fields = ['name', 'caste', 'occupations', 'place_of_residence']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}


class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ['name', 'caste', 'occupations', 'place_of_residence']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}


class LandBoughtForm(forms.ModelForm):
    class Meta:
        model = LandBought
        fields = ['household', 'year_of_purchase', 'extent', 'type_of_land', 'seller', 'price_of_land', 'comments']
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}


class LandSoldForm(forms.ModelForm):
    class Meta:
        model = LandSold
        fields = ['household', 'year_of_sale', 'extent', 'type_of_land', 'buyer', 'price_of_land', 'reasons_for_sale']
        exclude = ['household', 'buyer']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}
