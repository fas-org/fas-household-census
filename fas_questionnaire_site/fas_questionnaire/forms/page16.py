from django import forms

from fas_questionnaire.forms.common import ListTextWidget
from fas_questionnaire.models.common import Caste
from fas_questionnaire.models.page17 import ItemType
from fas_questionnaire.models.page6 import WhereMarketed, MarketingAgencies
from ..models.page16 import *


class IncomeFromStateAndCommonPropertyResourcesForm(forms.ModelForm):
    class Meta:
        model = IncomeFromStateAndCommonPropertyResources
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        super(IncomeFromStateAndCommonPropertyResourcesForm, self).__init__(*args, **kwargs)
        item_list = ItemType.objects.values_list('item')
        self.fields['item_collected'].widget = ListTextWidget(data_list=item_list, name='item-list')

        marketed_list = WhereMarketed.objects.values_list('place_of_market')
        self.fields['where_marketed'].widget = ListTextWidget(data_list=marketed_list, name='marketed-list')

        agencies_list = MarketingAgencies.objects.values_list('marketing_agency')
        self.fields['marketing_agency'].widget = ListTextWidget(data_list=agencies_list, name='agencies-list')


class FreedomOfEmploymentQuestionsForm(forms.ModelForm):
    class Meta:
        model = FreedomOfEmploymentQuestions
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}


class AgriculturalOrNonAgriculturalLabourServicesForm(forms.ModelForm):
    class Meta:
        model = AgriculturalOrNonAgriculturalLabourServices
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        super(AgriculturalOrNonAgriculturalLabourServicesForm, self).__init__(*args, **kwargs)
        caste_list = Caste.objects.values_list('caste')
        self.fields['caste_of_employer'].widget = ListTextWidget(data_list=caste_list, name='caste-list')
