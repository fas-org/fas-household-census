from django import forms
from ..models.page5 import *


class CroppingPatternAndCropScheduleForm(forms.ModelForm):
    class Meta:
        model = CroppingPatternAndCropSchedule
        fields = ['household',
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
        exclude = [
                   'unit_production',
                   'unit_consumption',
                   'loans_advances_taken_from_buyer',
                   'principal',
                   'interest_on_loans_advances',
                   'output_price_if_fixed_in_advance',
                   'other_conditions',
                   'household', 'crop_number_first_digit',
                   'crop_number_second_digit', 'crop_clean']
        widgets = None
        labels={
            'production_main_product': 'Grain/main product',
            'production_by_product': 'Straw and other by products',
            'consumption_main_product': 'Grain/main product',
            'consumption_by_product': 'Straw and other by products'
        }
        localized_fields = None
        help_texts = {}
        error_messages = {}


class CroppingPatternAndCropScheduleCommentsForm(forms.ModelForm):
    class Meta:
        model = CroppingPatternAndCropScheduleComments
        fields = ['household', 'comments_notes']
        exclude = ['household']
        widgets = {
            'comments_notes':forms.Textarea(attrs={'rows':10,'cols':198})
        }
        localized_fields = None
        help_texts = {}
        error_messages = {}
