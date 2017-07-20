from django import forms

from fas_questionnaire.forms.common import ListTextWidget
from fas_questionnaire.models.common import LandType, Caste, Occupation
from ..models.page3 import LandLeasedInOnFixedRent, Registration, TypeOfContract
from ..models.page3 import LandLeasedOutOnFixedRent


class LandLeasedInOnFixedRentForm(forms.ModelForm):
    class Meta:
        model = LandLeasedInOnFixedRent
        fields = ['household',
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
                  'any_loans_or_advances_from_owner',
                  'value_of_manure_provided_by_owner',
                  'value_of_fertiliser_provided_by_owner',
                  'value_of_seed_provided_by_owner',
                  'value_of_pesticide_provided_by_owner',
                  'value_of_electricity_provided_by_owner',
                  'if_pumpset_provided_by_owner',
                  'if_irrigation_provided_by_owner',
                  'if_machinery_provided_by_owner',
                  'comments']
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        super(LandLeasedInOnFixedRentForm, self).__init__(*args, **kwargs)
        type_of_land_purchased_list = LandType.objects.values_list('type')
        self.fields['land_type'].widget = ListTextWidget(data_list=type_of_land_purchased_list, name='type_of_land_purchased-list')
        caste_of_seller_list = Caste.objects.values_list('caste')
        self.fields['caste_of_lessor'].widget = ListTextWidget(data_list=caste_of_seller_list, name='caste_of_seller-list')
        registered_unregistered_list = Registration.objects.values_list('registration')
        self.fields['registered_unregistered'].widget = ListTextWidget(data_list=registered_unregistered_list, name='registered_unregistered_list')
        contract_list = TypeOfContract.objects.values_list('type_of_contract')
        self.fields['type_of_contract'].widget = ListTextWidget(data_list=contract_list, name='contract-list')
        occupation_of_lessor_list = Occupation.objects.values_list('occupation')
        self.fields['occupation_of_lessor'].widget = ListTextWidget(data_list=occupation_of_lessor_list,
                                                                   name='occupation_of_lessor-list')


class LandLeasedOutOnFixedRentForm(forms.ModelForm):
    class Meta:
        model = LandLeasedOutOnFixedRent
        fields = ['household',
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
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        super(LandLeasedOutOnFixedRentForm, self).__init__(*args, **kwargs)
        type_of_land_purchased_list = LandType.objects.values_list('type')
        self.fields['land_type'].widget = ListTextWidget(data_list=type_of_land_purchased_list, name='type_of_land_purchased-list')
        caste_of_seller_list = Caste.objects.values_list('caste')
        self.fields['caste_of_lessee'].widget = ListTextWidget(data_list=caste_of_seller_list,name='caste_of_seller-list')
        registered_unregistered_list = Registration.objects.values_list('registration')
        self.fields['registered_unregistered'].widget = ListTextWidget(data_list=registered_unregistered_list,name='registered_unregistered_list')
        contract_list = TypeOfContract.objects.values_list('type_of_contract')
        self.fields['type_of_contract'].widget = ListTextWidget(data_list=contract_list, name='contract-list')
        occupation_of_lessee_list = Occupation.objects.values_list('occupation')
        self.fields['occupation_of_lessee'].widget = ListTextWidget(data_list=occupation_of_lessee_list,
                                                                   name='occupation_of_lessee-list')
