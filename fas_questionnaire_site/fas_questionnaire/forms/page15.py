from django import forms

from fas_questionnaire.forms.common import ListTextWidget
from fas_questionnaire.models.common import YesOrNo, PlaceOfWork
from ..models.page15 import *


class LongTermWorkersForm(forms.ModelForm):
    class Meta:
        model = LongTermWorkers
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        super(LongTermWorkersForm, self).__init__(*args, **kwargs)
        caste_list = Caste.objects.values_list('caste')
        self.fields['caste'].widget = ListTextWidget(data_list=caste_list, name='caste-list')

        occupation_list = Occupation.objects.values_list('occupation')
        self.fields['occupation'].widget = ListTextWidget(data_list=occupation_list, name='occupation_list')

        agricultural_labour_yes_or_no = YesOrNo.objects.values_list('title')
        self.fields['agricultural_labor'].widget = ListTextWidget(data_list=agricultural_labour_yes_or_no, name='agricultural_labour_yes_or_no')

        operating_machines_yes_or_no = YesOrNo.objects.values_list('title')
        self.fields['operating_machines'].widget = ListTextWidget(data_list=operating_machines_yes_or_no, name='operating_machines_yes_or_no')

        tending_animals_yes_or_no = YesOrNo.objects.values_list('title')
        self.fields['tending_animals'].widget = ListTextWidget(data_list=tending_animals_yes_or_no, name='tending_animals_yes_or_no')

        non_agri_business_yes_or_no = YesOrNo.objects.values_list('title')
        self.fields['non_agri_business'].widget = ListTextWidget(data_list=non_agri_business_yes_or_no, name='non_agri_business_yes_or_no')

        work_description_list = WorkDescription.objects.values_list('description')
        self.fields['domestic_work'].widget = ListTextWidget(data_list=work_description_list, name='work_description_list')


class NonAgricultureWorkersForm(forms.ModelForm):
    class Meta:
        model = NonAgricultureWorkers
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        super(NonAgricultureWorkersForm, self).__init__(*args, **kwargs)
        works_list = WorkDescription.objects.values_list('description')
        self.fields['work_description'].widget = ListTextWidget(data_list=works_list, name='works_list')

        work_place_list = PlaceOfWork.objects.values_list('place')
        self.fields['work_place'].widget = ListTextWidget(data_list=work_place_list, name='work_place_list')

        wage_form_list = WageType.objects.values_list('type')
        self.fields['wage_form'].widget = ListTextWidget(data_list=wage_form_list, name='wage_non_form_list')
        # work_place_list = PlaceOfWork.objects.values_list('place')
        # self.fields['work_place'].widget = ListTextWidget(data_list=work_place_list, name='work_place_list')
