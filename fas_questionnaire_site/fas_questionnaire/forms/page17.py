from django import forms

from fas_questionnaire.forms.common import ListTextWidget
from ..models.page17 import *


class IncomeFromSalariesForm(forms.ModelForm):
    class Meta:
        model = IncomeFromSalaries
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}


class IncomeFromOtherBusinessActivitiesForm(forms.ModelForm):
    class Meta:
        model = IncomeFromOtherBusinessActivities
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}


class AnimalResoursesInventoryForm(forms.ModelForm):
    class Meta:
        model = AnimalResoursesInventory
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        super(AnimalResoursesInventoryForm, self).__init__(*args, **kwargs)
        inventory_list = AnimalTypes.objects.values_list('name')
        self.fields['type'].widget = ListTextWidget(data_list=inventory_list, name='inventory-list')
        sex_list = Sex.objects.values_list('sex')
        self.fields['sex'].widget = ListTextWidget(data_list=sex_list, name='inventory_sex-list')
        cattle_type_list = AnimalCattleType.objects.values_list('type')
        self.fields['cattle_type'].widget = ListTextWidget(data_list=cattle_type_list, name='cattle_type-list')


class AnimalResourcesFeedForm(forms.ModelForm):
    class Meta:
        model = AnimalResourcesFeed
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        super(AnimalResourcesFeedForm, self).__init__(*args, **kwargs)
        type_of_feed_list = FeedType.objects.values_list('feed_name')
        self.fields['type_of_feed'].widget = ListTextWidget(data_list=type_of_feed_list, name='type_of_feed-list')
        feed_source_list = FeedSource.objects.values_list('source')
        self.fields['source'].widget = ListTextWidget(data_list=feed_source_list, name='feed_source-list')


class OtherExpendituresForm(forms.ModelForm):
    class Meta:
        model = OtherExpenditure
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self,*args,**kwargs):
        super(OtherExpendituresForm,self).__init__(*args,**kwargs)
        expenditure_item_list = ItemType.objects.values_list('item')
        self.fields['item'].widget = ListTextWidget(data_list=expenditure_item_list, name='expenditure_item-list')


class OutputAndIncomeForm(forms.ModelForm):
    class Meta:
        model = OutputAndIncome
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self,*args,**kwargs):
        super(OutputAndIncomeForm,self).__init__(*args,**kwargs)
        output_product_list = ProductType.objects.values_list('product_name')
        self.fields['product'].widget = ListTextWidget(data_list=output_product_list, name='output_product-list')
        production_unit_list = Units.objects.values_list('unit')
        self.fields['production_unit'].widget = ListTextWidget(data_list=production_unit_list, name='production_unit-list')
        sale_unit_list = Units.objects.values_list('unit')
        self.fields['sale_unit'].widget = ListTextWidget(data_list=sale_unit_list, name='sale_unit-list')
        price_unit_list = Units.objects.values_list('unit')
        self.fields['price_unit'].widget = ListTextWidget(data_list=price_unit_list, name='price_unit-list')





