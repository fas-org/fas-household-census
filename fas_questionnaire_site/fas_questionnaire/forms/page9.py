from django import forms

from fas_questionnaire.forms.common import ListTextWidget
from fas_questionnaire.models.common import Crop
from ..models.page9 import *


class OwnershipTypeForm(forms.ModelForm):

    class Meta:
        model = OwnershipType
        fields = ['type']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}


class WellTypeForm(forms.ModelForm):

    class Meta:
        model = WellType
        fields = ['type']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}


class PowerSourceForm(forms.ModelForm):

    class Meta:
        model = PowerSource
        fields = ['source']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}


class ExchangeNatureForm(forms.ModelForm):

    class Meta:
        model = NatureExchange
        fields = ['exchange']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}


class OwnershipWellsTubewellsForm(forms.ModelForm):

    class Meta:
        model = OwnershipWellsTubewells
        fields = ['household','sno', 'ownership_type', 'year_when_installed', 'present_depth', 'original_depth', 'type', 'power_source', 'installation_cost', 'finance_source', 'expenses_last_year', 'irrigation_crop', 'irrigation_sale_area', 'irrigation_revenue', 'exchange_nature', 'irrigation_land_extent', 'comments']
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages  = {}

    def __init__(self, *args, **kwargs):
        super(OwnershipWellsTubewellsForm, self).__init__(*args, **kwargs)
        ownership_type_list = OwnershipType.objects.values_list('type')
        self.fields['ownership_type'].widget = ListTextWidget(data_list=ownership_type_list, name='ownership_type-list')
        wellType_list = WellType.objects.values_list('type')
        self.fields['type'].widget = ListTextWidget(data_list=wellType_list, name='wellType-list')
        power_source_list = PowerSource.objects.values_list('source')
        self.fields['power_source'].widget = ListTextWidget(data_list=power_source_list, name='power_source-list')
        finance_source_list = SourceOfFinance.objects.values_list('source')
        self.fields['finance_source'].widget = ListTextWidget(data_list=finance_source_list, name='finance_source-list')
        irrigation_crop_list = Crop.objects.values_list('name')
        self.fields['irrigation_crop'].widget = ListTextWidget(data_list=irrigation_crop_list, name='irrigation_crop-list')
        exchange_nature_list = NatureExchange.objects.values_list('exchange')
        self.fields['exchange_nature'].widget = ListTextWidget(data_list=exchange_nature_list, name='exchange_nature-list')




class SpecifiedProductionMeansForm(forms.ModelForm):

    class Meta:
        model = SpecifiedProductionMeans
        fields = ['household','production_item_code', 'ownership_number', 'year_of_purchase', 'price_paid', 'subsidy_received', 'present_value', 'maintenance_charges', 'rental_earnings', 'rental_earnings_units', 'comments']
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        super(SpecifiedProductionMeansForm, self).__init__(*args, **kwargs)
        production_item_code_list = ProductionMeans.objects.values_list('type')
        self.fields['irrigation_item_code'].widget = ListTextWidget(data_list=production_item_code_list, name='production_item_code-list')
        rental_earnings_units_list = Units.objects.values_list('unit')
        self.fields['rental_earnings_units'].widget = ListTextWidget(data_list=rental_earnings_units_list, name='rental_earnings_units-list')




class SpecifiedIrrigationMeansForm(forms.ModelForm):

    class Meta:
        model = SpecifiedProductionMeans
        fields = ['household','irrigation_item_code', 'ownership_number', 'year_of_purchase', 'price_paid', 'subsidy_received', 'present_value', 'maintenance_charges', 'rental_earnings', 'rental_earnings_units', 'comments']
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self,*args,**kwargs):
        super(SpecifiedIrrigationMeansForm,self).__init__(*args,**kwargs)
        irrigation_item_code_list = IrrigationFlow.objects.values_list('type')
        self.fields['irrigation_item_code'].widget = ListTextWidget(data_list=irrigation_item_code_list, name='irrigation_item_code-list')




