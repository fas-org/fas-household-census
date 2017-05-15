from django import forms

from fas_questionnaire.forms.common import ListTextWidget
from ..models.page6 import *


class SalesOfCropProducedForm(forms.ModelForm):
    class Meta:
        model = SalesOfProduction
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self,*args,**kwargs):
        super(SalesOfCropProducedForm,self).__init__(*args,**kwargs)
        unit_of_quantity_list = Units.objects.values_list('unit')
        self.fields['unit_of_quantity'].widget = ListTextWidget(data_list=unit_of_quantity_list, name='unit_of_quantity-list')

        month_of_disposal_list = Month.objects.values_list('month')
        self.fields['month_of_disposal'].widget = ListTextWidget(data_list=month_of_disposal_list, name='month_of_disposal-list')

        unit_of_price_list = Units.objects.values_list('unit')
        self.fields['unit_of_price'].widget = ListTextWidget(data_list=unit_of_price_list, name='unit_of_price-list')

        where_marketed_list = WhereMarketed.objects.values_list('place_of_market')
        self.fields['where_marketed'].widget = ListTextWidget(data_list=where_marketed_list, name='where_marketed-list')

        marketing_agency_list = MarketingAgencies.objects.values_list('marketing_agency')
        self.fields['marketing_agency'].widget = ListTextWidget(data_list=marketing_agency_list, name='marketing_agency-list')

        if_price_determined_in_advance_list = YesOrNo.objects.values_list('title')
        self.fields['if_price_determined_in_advance'].widget = ListTextWidget(data_list=if_price_determined_in_advance_list, name='if_price_determined_in_advance-list')





class ProductionForm(forms.ModelForm):
    class Meta:
        model = Production
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        super(ProductionForm, self).__init__(*args, **kwargs)
        crop_list = Crop.objects.values_list('name')
        self.fields['crop'].widget = ListTextWidget(data_list=crop_list, name='production_crop_list-list')

        unit_main_production_list = Units.objects.values_list('unit')
        self.fields['unit_main_production'].widget = ListTextWidget(data_list=unit_main_production_list, name='unit_main_production-list')

        unit_by_production_list = Units.objects.values_list('unit')
        self.fields['unit_by_production'].widget = ListTextWidget(data_list=unit_by_production_list, name='unit_by_production-list')

        unit_main_consumption_list = Units.objects.values_list('unit')
        self.fields['unit_main_consumption'].widget = ListTextWidget(data_list=unit_main_consumption_list, name='unit_main_consumption-list')

        unit_by_consumption_list = Units.objects.values_list('unit')
        self.fields['unit_by_consumption'].widget = ListTextWidget(data_list=unit_by_consumption_list, name='unit_by_consumption-list')

        unit_main_rent_and_wages_list = Units.objects.values_list('unit')
        self.fields['unit_main_rent_and_wages'].widget = ListTextWidget(data_list=unit_main_rent_and_wages_list, name='unit_main_rent_and_wages-list')

        unit_by_rent_and_wages_list = Units.objects.values_list('unit')
        self.fields['unit_by_rent_and_wages'].widget = ListTextWidget(data_list=unit_by_rent_and_wages_list, name='unit_by_rent_and_wages-list')


