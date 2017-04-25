from django import forms
from ..models.page3 import LandLeasedInOnFixedRent
from ..models.page3 import LandLeasedOutOnFixedRent


class LandLeasedInOnFixedRentForm(forms.ModelForm):
    class Meta:
        model = LandLeasedInOnFixedRent
        fields = ['household_number',
                  'plot_no',
                  'land_type',
                  'extent',
                  'unit_of_extent',
                  'name_of_lessor',
                  'caste_of_lessor',
                  'occupation_of_lessor',
                  'registered_unregistered',
                  'type_of_contract',
                  'since_when_leased_in',
                  'annual_rent_in_cash',
                  'annual_rent_in_kind',
                  'interest_free_borrowing',
                  'loan_with_interest',
                  'further_interest_payment_on_rent',
                  'qty_of_hay_taken_by_owner',
                  'value_of_manure_provided_by_owner',
                  'value_of_fertiliser_provided_by_owner',
                  'value_of_seed_provided_by_owner',
                  'value_of_pesticide_provided_by_owner',
                  'value_of_electricity_provided_by_owner',
                  'if_pumpset_provided_by_owner',
                  'if_irrigation_provided_by_owner',
                  'if_machinery_provided_by_owner',
                  'comments']
        exclude = ['household_number']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}


class LandLeasedOutOnFixedRentForm(forms.ModelForm):
    class Meta:
        model = LandLeasedOutOnFixedRent
        fields = ['household_number',
                  'ownership_plot_no',
                  'land_type',
                  'extent',
                  'unit_of_extent',
                  'name_of_lessee',
                  'caste_of_lessee',
                  'occupation_of_lessee',
                  'registered_unregistered',
                  'type_of_contract',
                  'since_when_leased_out',
                  'annual_rent_in_cash',
                  'annual_rent_in_kind',
                  'interest_free_loan_given',
                  'loan_with_interest_given',
                  'further_interest_on_rent',
                  'qty_of_hay_taken',
                  'value_of_manure_provided_by_you',
                  'value_of_fertiliser_provided_by_you',
                  'value_of_seed_provided_by_you',
                  'value_of_pesticide_provided_by_you',
                  'value_of_electricity_paid_for_by_you',
                  'if_you_provided_the_pumpset',
                  'if_irrigation_provided_by_owner',
                  'if_machinery_provided_by_owner',
                  'comments']
        exclude = ['household_number']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}



