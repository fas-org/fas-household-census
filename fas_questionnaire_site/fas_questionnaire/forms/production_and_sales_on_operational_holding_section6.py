from django import forms
from ..models.production_and_sales_on_operational_holding_section6 import CropProductionOnOperationalHolding
from ..models.production_and_sales_on_operational_holding_section6 import CropProductionOnOperationalHoldingComments


class CropProductionOnOperationalHoldingForm(forms.ModelForm):
    class Meta:
        model = CropProductionOnOperationalHolding
        fields = ['id',
                  'household',
                  'serial_no',
                  'crop_number_first_digit',
                  'crop_number_second_digit',
                  'crop',
                  'crop_clean',
                  'variety',
                  'tenurial_status',
                  'crop_homestead_land',
                  'extent',
                  'month_of_sowing',
                  'month_of_harvesting',
                  'source_of_irrigation',
                  'production_main_product',
                  'unit_production',
                  'production_by_product',
                  'consumption_main_product',
                  'unit_consumption',
                  'consumption_by_product',
                  'loans_advances_taken_from_buyer',
                  'principal',
                  'interest_on_loans_advances',
                  'output_price_if_fixed_in_advance',
                  'other_conditions',
                  'comments']
        exclude = ['production_main_product',
                   'unit_production',
                   'production_by_product',
                   'consumption_main_product',
                   'unit_consumption',
                   'consumption_by_product',
                   'loans_advances_taken_from_buyer',
                   'principal',
                   'interest_on_loans_advances',
                   'output_price_if_fixed_in_advance',
                   'other_conditions',
                   'household', 'crop_number_first_digit',
                   'crop_number_second_digit', 'crop_clean']
        widgets = None
        localized_fields = None
        help_texts = {}
        error_messages = {}


class CropProductionOnOperationalHoldingCommentsForm(forms.ModelForm):
    class Meta:
        model = CropProductionOnOperationalHoldingComments
        fields = ['household', 'comments_notes']
        exclude = ['household']
        widgets = None
        localized_fields = None
        help_texts = {}
        error_messages = {}
