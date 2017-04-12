from django import forms
from ..models.production_and_sales_on_operational_holding_section6 import CroppingPatternAndCropSchedule
from ..models.production_and_sales_on_operational_holding_section6 import CroppingPatternAndCropScheduleComments
from ..models.production_and_sales_on_operational_holding_section6 import ProductionAndSales


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
                   'CONSUMPTION_MAIN_PRODUCT',
                   'consumption_by_product',
                   'production_main_product',
                   'production_by_product',
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
        localized_fields = None
        help_texts = {}
        error_messages = {}


class CroppingPatternAndCropScheduleCommentsForm(forms.ModelForm):
    class Meta:
        model = CroppingPatternAndCropScheduleComments
        fields = ['household', 'comments_notes']
        exclude = ['household']
        widgets = None
        localized_fields = None
        help_texts = {}
        error_messages = {}

class  ProductionAndSalesForm(forms.ModelForm):
    class Meta:
        model= ProductionAndSales
        fields=['crop_serial_no',
                'sales_of_main_product_transportation_mode',
                'sales_of_main_product_transportation_cost',
                'sales_of_main_product_other_marketing_costs',
                'sales_of_by_product_amt',
                'sales_of_by_product_price',
                'quantity_of_main_product_used_for_payment',
                'quantity_of_by_product_used_for_payment',
                'household',
                'crop_number_first_digit',
                'crop_number_second_digit',
                'sale_number',
                'commodity_sold',
                'month_of_disposal',
                'quantity',
                'unit_of_quantity',
                'price',
                'unit_of_price',
                'where_marketed',
                'marketing_agency',
                'marketing_agency_value',
                'if_price_determined_in_advance',
                'consumption_main_product',
                'consumption_by_product',
                'production_main_product',
                'production_by_product'
                ]
        exclude=['unit_of_quantity',
                 'unit_of_price',
                 'commodity_sold','household',
                 'comments'
                 ]
        widgets=None
        localized_fields = None
        labels = {
            'crop_serial_no':'Serial no',
            'sales_of_main_product_transportation_mode':'Mode',
            'sales_of_main_product_transportation_cost':'Cost Incurred',
            'sales_of_main_product_other_marketing_costs':'Other marketing Costs',
            'if_price_determined_in_advance':'Was the price fixed before harvesting',
            'sales_of_by_product_amt':'Amt',
            'sales_of_by_product_price':'Price',
            'quantity_of_main_product_used_for_payment':'Grain/Main product',
            'quantity_of_by_product_used_for_payment':'Straw and other by-products',
            'production_main_product':'Grain/main product',
            'production_by_product': 'Straw and other by products',
            'consumption_main_product': 'Grain/main product',
            'consumption_by_product': 'Straw and other by products'
        }
        help_texts = {}
        error_messages = {}
