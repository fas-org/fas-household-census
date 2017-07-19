from django import forms

from fas_questionnaire.forms.common import ListTextWidget
from fas_questionnaire.models.common import Units
from fas_questionnaire.models.page2 import IrrigationSource
from ..models.page7 import InputUseSeeds, InputUseFertiliser, InputUseManure, InputUsePlantProtection, \
    InputUseIrrigation, ManureType, FertilizerType, UnitPrice


class InputUseManureForm(forms.ModelForm):
    class Meta:
        model = InputUseManure
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self,*args,**kwargs):
        super(InputUseManureForm,self).__init__(*args,**kwargs)

        manure_type_list = ManureType.objects.values_list('type')
        self.fields['manure_type'].widget = ListTextWidget(data_list=manure_type_list, name='manure_type-list')

        manure_home_unit_list = Units.objects.values_list('unit')
        self.fields['manure_home_unit'].widget = ListTextWidget(data_list=manure_home_unit_list, name='manure_home_unit-list')

        manure_purchased_unit_list = Units.objects.values_list('unit')
        self.fields['manure_purchased_unit'].widget = ListTextWidget(data_list=manure_purchased_unit_list, name='manure_purchased_unit-list')



class InputUsePlantProtectionForm(forms.ModelForm):
    class Meta:
        model = InputUsePlantProtection
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}


class InputUseIrrigationForm(forms.ModelForm):
    class Meta:
        model = InputUseIrrigation
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self,*args,**kwargs):
        super(InputUseIrrigationForm,self).__init__(*args,**kwargs)

        irrigation_source_list = IrrigationSource.objects.values_list('source')
        self.fields['irrigation_source'].widget = ListTextWidget(data_list=irrigation_source_list, name='irrigation_source_list')

        irrigation_unit_price_list = UnitPrice.objects.values_list('unit_price')
        self.fields['irrigation_unit_price'].widget = ListTextWidget(data_list=irrigation_unit_price_list, name='irrigation_unit_price_list')


class InputUseFertiliserForm(forms.ModelForm):
    class Meta:
        model = InputUseFertiliser
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self,*args,**kwargs):
        super(InputUseFertiliserForm,self).__init__(*args,**kwargs)

        fertiliser_type_list = FertilizerType.objects.values_list('type')
        self.fields['fertiliser_type'].widget = ListTextWidget(data_list=fertiliser_type_list, name='fertiliser_type-list')

        fertiliser_unit_list = Units.objects.values_list('unit')
        self.fields['fertiliser_unit'].widget = ListTextWidget(data_list=fertiliser_unit_list, name='fertiliser_unit_list')


class InputUseSeedsForm(forms.ModelForm):
    class Meta:
        model = InputUseSeeds
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self,*args,**kwargs):
        super(InputUseSeedsForm,self).__init__(*args,**kwargs)

        home_produced_unit_list = Units.objects.values_list('unit')
        self.fields['home_produced_unit'].widget = ListTextWidget(data_list=home_produced_unit_list, name='home_produced_unit_list')

        purchased_unit_list = Units.objects.values_list('unit')
        self.fields['purchased_unit'].widget = ListTextWidget(data_list=purchased_unit_list, name='purchased_unit_list')
