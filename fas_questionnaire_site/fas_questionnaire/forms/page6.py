from django import forms
from ..models.page6 import *


class ProductionAndSalesForm(forms.ModelForm):
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
            'quantity_of_by_product_used_for_payment':'Straw and other by-products'
        }
        help_texts = {}
        error_messages = {}
