from django import forms
from ..models.page5 import *


class CroppingPatternAndCropScheduleForm(forms.ModelForm):
    class Meta:
        model = CroppingPatternAndCropSchedule
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
        exclude = ['household']
        widgets = {
            'comments_notes':forms.Textarea(attrs={'rows':10,'cols':198})
        }
        localized_fields = None
        help_texts = {}
        error_messages = {}
