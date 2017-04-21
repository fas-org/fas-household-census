from django import forms
from ..models.page6 import *


class ProductionAndSalesForm(forms.ModelForm):
    class Meta:
        model= ProductionAndSales
        fields=['crop_serial_no', 'crop',
                'sales_of_main_product_transportation_mode',
                'sales_of_main_product_transportation_cost',
                'sales_of_main_product_other_marketing_costs',
                'sales_of_by_product_amt',
                'sales_of_by_product_price',
                'quantity_of_main_product_used_for_payment',
                'quantity_of_by_product_used_for_payment',
                'household',
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
                'comments'
                ]
        exclude=['household'
                 ]
        widgets=None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def clean(self):
        if self.cleaned_data.get('crop_serial_no') is None :
            raise forms.ValidationError('Please select serial number')
        return self.cleaned_data

