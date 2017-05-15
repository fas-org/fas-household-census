from django import forms

from fas_questionnaire.forms.common import ListTextWidget
from ..models.page_13 import PatternOfAgriculturalLabouringOut, TypeOfWage, WageUnit
from ..models.common import Crop, Sex, PlaceOfWork
from ..models.page1 import HouseholdMembers


class PatternOfAgriculturalLabouringOutForm(forms.ModelForm):
    """Pattern of Agricultural Labouring Out Form"""
    class Meta:
        model = PatternOfAgriculturalLabouringOut
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        super(PatternOfAgriculturalLabouringOutForm, self).__init__(*args, **kwargs)
        sex_list = Sex.objects.values_list('sex')
        self.fields['sex'].widget = ListTextWidget(data_list=sex_list, name='sex_list')

        crop_list = Crop.objects.values_list('name')
        self.fields['crop'].widget = ListTextWidget(data_list=crop_list, name='crop_list')

        wages_list = TypeOfWage.objects.values_list('type')
        self.fields['type_of_wage'].widget = ListTextWidget(data_list=wages_list, name='wages_list')

        places_list = PlaceOfWork.objects.values_list('place')
        self.fields['place_of_work'].widget = ListTextWidget(data_list=places_list, name='places_list')

        wage_unit_list = WageUnit.objects.values_list('unit')
        self.fields['unit'].widget = ListTextWidget(data_list=wage_unit_list, name='wage_unit_list')

