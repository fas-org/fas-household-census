from django import forms
from ..models.page4 import LandMortgagedIn
from ..models.page4 import LandMortgagedOut
from ..models.page4 import LandLeasedInOnShareRent
from ..models.page4 import LandLeasedOutOnShareRent


class LandMortgagedInForm(forms.ModelForm):
    class Meta:
        model = LandMortgagedIn
        fields = ['household',
                  'land_type',
                  'extent',
                  'name_of_mortgagor',
                  'caste_of_mortgagor',
                  'occupation_of_mortgagor',
                  'year_of_mortgage',
                  'mortgage_period',
                  'mortgage_money',
                  'interest_usufruct',
                  'comments']
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

class LandMortgagedOutForm(forms.ModelForm):
    class Meta:
        model = LandMortgagedOut
        fields = ['household',
                  'land_type',
                  'extent',
                  'name_of_mortgagee',
                  'caste_of_mortgagee',
                  'occupation_of_mortgagee',
                  'year_of_mortgage',
                  'mortgage_period',
                  'mortgage_money',
                  'interest_usufruct',
                  'comments']
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}


class LandLeasedInOnShareRentForm(forms.ModelForm):
    class Meta:
        model = LandLeasedInOnShareRent
        fields = ['household',
                  'operational_plot_no',
                  'land_type',
                  'extent',
                  'unit_of_extent',
                  'name_of_lessor',
                  'caste_of_lessor',
                  'occupation_of_lessor',
                  'registered_unregistered',
                  'seasonal_yearly_other',
                  'year_of_lease',
                  'percentage_share_of_crop',
                  'quantity_share_of_crop',
                  'percentage_share_of_by_product',
                  'quantity_share_in_by_product',
                  'share_in_fym_field',
                  'share_in_fym_quantity_field',
                  'share_in_fertiliser_field',
                  'share_in_fertiliser_quantity_field',
                  'share_in_seed_field',
                  'share_in_seed_quantity_field',
                  'share_in_pesticide_field',
                  'share_in_pesticide_quantity_field',
                  'share_in_electricity_field',
                  'share_in_electricity_quantity_field',
                  'share_in_pumpset_field',
                  'share_in_pumpset_rs_field',
                  'share_in_labour_field',
                  'share_in_labour_quantity_field',
                  'share_in_irrigation_field',
                  'share_in_irrigation_rs_field',
                  'share_in_machinery_field',
                  'share_in_machinery_quantity_field',
                  'interest_free_loan_by_owner',
                  'amount_of_other_loan',
                  'interest_of_other_loan',
                  'comment',]
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}


class LandLeasedOutOnShareRentForm(forms.ModelForm):
    class Meta:
        model = LandLeasedOutOnShareRent
        fields = ['household',
                  'ownership_plot_no',
                  'land_type',
                  'extent',
                  'unit_of_extent',
                  'name_of_sharecropper',
                  'caste_of_sharecropper',
                  'occupation_of_sharecropper',
                  'registered_unregistered',
                  'seasonal_annual_other',
                  'year_of_lease',
                  'percentage_share_of_crop',
                  'quantity_share_of_crop',
                  'percentage_share_of_by_product',
                  'quantity_share_of_by_product',
                  'share_in_fym_field',
                  'share_in_fym_rs_field',
                  'share_in_fertiliser_field',
                  'share_in_fertiliser_rs_field',
                  'share_in_seed_field',
                  'share_in_seed_rs_field',
                  'share_in_pesticide_field',
                  'share_in_pesticide_rs_field',
                  'share_in_electricity_field',
                  'share_in_electricity_rs_field',
                  'share_in_pumpset_field',
                  'share_in_pumpset_rs_field',
                  'share_in_labour_field',
                  'share_in_labour_quantity_field',
                  'share_in_irrigation_field',
                  'share_in_irrigation_rs_field',
                  'share_in_machinery_field',
                  'share_in_machinery_quantity_field',
                  'interest_free_loan_by_owner',
                  'amount_of_other_loan',
                  'interest_of_other_loan',
                  'comment']
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}