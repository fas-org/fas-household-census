from django import forms

from fas_questionnaire.forms.common import ListTextWidget
from fas_questionnaire.models.common import LandType, Caste, Occupation
from fas_questionnaire.models.page3 import Registration
from ..models.page4 import LandMortgagedIn, InterestUsufruct, SeasonalYearlyOther
from ..models.page4 import LandMortgagedOut
from ..models.page4 import LandLeasedInOnShareRent
from ..models.page4 import LandLeasedOutOnShareRent


class LandMortgagedInForm(forms.ModelForm):
    class Meta:
        model = LandMortgagedIn
        fields = ['household',
                  'sno',
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

    def __init__(self, *args, **kwargs):
        super(LandMortgagedInForm, self).__init__(*args, **kwargs)
        type_of_land_purchased_list = LandType.objects.values_list('type')
        self.fields['land_type'].widget = ListTextWidget(data_list=type_of_land_purchased_list,name='type_of_land_purchased-list')
        caste_of_seller_list = Caste.objects.values_list('caste')
        self.fields['caste_of_mortgagor'].widget = ListTextWidget(data_list=caste_of_seller_list,name='caste_of_seller-list')
        occupation_of_buyer_list = Occupation.objects.values_list('occupation')
        self.fields['occupation_of_mortgagor'].widget = ListTextWidget(data_list=occupation_of_buyer_list,
                                                                       name='occupation_of_buyer-list')
        interest_usufruct_list = InterestUsufruct.objects.values_list('interestusufruct')
        self.fields['interest_usufruct'].widget = ListTextWidget(data_list=interest_usufruct_list,
                                                                       name='interest_usufruct-list')

class LandMortgagedOutForm(forms.ModelForm):
    class Meta:
        model = LandMortgagedOut
        fields = ['household',
                  'sno',
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

    def __init__(self, *args, **kwargs):
        super(LandMortgagedOutForm, self).__init__(*args, **kwargs)
        type_of_land_purchased_list = LandType.objects.values_list('type')
        self.fields['land_type'].widget = ListTextWidget(data_list=type_of_land_purchased_list,
                                                         name='type_of_land_purchased-list')
        caste_of_seller_list = Caste.objects.values_list('caste')
        self.fields['caste_of_mortgagee'].widget = ListTextWidget(data_list=caste_of_seller_list,
                                                                  name='caste_of_seller-list')
        occupation_of_buyer_list = Occupation.objects.values_list('occupation')
        self.fields['occupation_of_mortgagee'].widget = ListTextWidget(data_list=occupation_of_buyer_list,
                                                                       name='occupation_of_buyer-list')
        interest_usufruct_list = InterestUsufruct.objects.values_list('interestusufruct')
        self.fields['interest_usufruct'].widget = ListTextWidget(data_list=interest_usufruct_list,
                                                                 name='interest_usufruct-list')

class LandLeasedInOnShareRentForm(forms.ModelForm):
    class Meta:
        model = LandLeasedInOnShareRent
        fields = ['household',
                  'sno',
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
                  'comments',]
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        super(LandLeasedInOnShareRentForm, self).__init__(*args, **kwargs)
        type_of_land_purchased_list = LandType.objects.values_list('type')
        self.fields['land_type'].widget = ListTextWidget(data_list=type_of_land_purchased_list,
                                                         name='type_of_land_purchased-list')
        caste_list = Caste.objects.values_list('caste')
        self.fields['caste_of_lessor'].widget = ListTextWidget(data_list=caste_list,
                                                                  name='caste-list')
        occupation_of_lessor_list = Occupation.objects.values_list('occupation')
        self.fields['occupation_of_lessor'].widget = ListTextWidget(data_list=occupation_of_lessor_list,
                                                                       name='occupation_of_lessor_list')
        registration_list = Registration.objects.values_list('registration')
        self.fields['registered_unregistered'].widget = ListTextWidget(data_list=registration_list,
                                                                    name='registration_list')
        season_list = SeasonalYearlyOther.objects.values_list('seasonalyearlyother')
        self.fields['seasonal_yearly_other'].widget = ListTextWidget(data_list=season_list,
                                                                       name='seasons')


class LandLeasedOutOnShareRentForm(forms.ModelForm):
    class Meta:
        model = LandLeasedOutOnShareRent
        fields = ['household',
                  'sno',
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
                  'comments']
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        super(LandLeasedOutOnShareRentForm, self).__init__(*args, **kwargs)
        type_of_land_purchased_list = LandType.objects.values_list('type')
        self.fields['land_type'].widget = ListTextWidget(data_list=type_of_land_purchased_list,
                                                         name='type_of_land_purchased-list')
        caste_list = Caste.objects.values_list('caste')
        self.fields['caste_of_sharecropper'].widget = ListTextWidget(data_list=caste_list,
                                                                  name='caste-list')
        occupation_of_sharecropper_list = Occupation.objects.values_list('occupation')
        self.fields['occupation_of_sharecropper'].widget = ListTextWidget(data_list=occupation_of_sharecropper_list,
                                                                       name='occupation_of_lessor_list')
        registration_list = Registration.objects.values_list('registration')
        self.fields['registered_unregistered'].widget = ListTextWidget(data_list=registration_list,
                                                                    name='registration_list')
        season_list = SeasonalYearlyOther.objects.values_list('seasonalyearlyother')
        self.fields['seasonal_annual_other'].widget = ListTextWidget(data_list=season_list,
                                                                       name='seasons')