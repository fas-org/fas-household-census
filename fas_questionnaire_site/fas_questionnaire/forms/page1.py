from django import forms

from fas_questionnaire.forms.common import ListTextWidget
from fas_questionnaire.models.common import Caste, Sex, Occupation, Relationship, PlaceOfWork
from ..models.page1 import HouseholdIntroduction, HouseholdMembers, Religion, TehsilOfBirth, CalendarGranularity, \
    MaritalStatus, LiteracyStatus, Education, BirthVillage, BirthDistrict, SC_ST_others


class HouseholdIntroductionForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = HouseholdIntroduction
        exclude = ['household']
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        super(HouseholdIntroductionForm, self).__init__(*args, **kwargs)
        caste_list = Caste.objects.values_list('caste')
        self.fields['caste_tribe'].widget = ListTextWidget(data_list=caste_list, name='caste-list')
        sex_list = Sex.objects.values_list('sex')
        self.fields['sex'].widget = ListTextWidget(data_list=sex_list, name='sex-list')
        religion_list = Religion.objects.values_list('religion')
        self.fields['religion'].widget = ListTextWidget(data_list=religion_list, name='religion-list')
        father_occupation_list = Occupation.objects.values_list('occupation')
        self.fields['father_occupation'].widget = ListTextWidget(data_list=father_occupation_list, name='father_occupation-list')
        tehsil_of_birth_list = TehsilOfBirth.objects.values_list('tehsil')
        self.fields['birth_tehsil'].widget = ListTextWidget(data_list=tehsil_of_birth_list, name='birth_tehsil-list')
        birth_village_list = BirthVillage.objects.values_list('villageName')
        self.fields['birth_village'].widget = ListTextWidget(data_list=birth_village_list, name='birth-village-list')
        birth_district_list = BirthDistrict.objects.values_list('name')
        self.fields['birth_district'].widget = ListTextWidget(data_list=birth_district_list, name='birth_district_list')
        SC_ST_list = SC_ST_others.objects.values_list('caste')
        self.fields['sc_st_others'].widget = ListTextWidget(data_list=SC_ST_list, name='SC_ST_list')


class HouseholdMembersForm(forms.ModelForm):
    class Meta:
        model = HouseholdMembers
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self,*args,**kwargs):
        super(HouseholdMembersForm,self).__init__(*args,**kwargs)
        sex_list = Sex.objects.values_list('sex')
        self.fields['sex'].widget = ListTextWidget(data_list=sex_list, name='sex-list')
        calender_granularity_list = CalendarGranularity.objects.values_list('unit')
        self.fields['age_unit'].widget = ListTextWidget(data_list=calender_granularity_list, name='calender_granularity-list')
        relationship_list = Relationship.objects.values_list('relationship')
        self.fields['relationship'].widget = ListTextWidget(data_list=relationship_list, name='relationship-list')
        marital_status_list = MaritalStatus.objects.values_list('status')
        self.fields['marital_status'].widget = ListTextWidget(data_list=marital_status_list, name='marital_status-list')
        primary_occupation_list = Occupation.objects.values_list('occupation')
        self.fields['primary_occupation'].widget = ListTextWidget(data_list=primary_occupation_list, name='primary_occupation-list')
        secondary_occupation_list = Occupation.objects.values_list('occupation')
        self.fields['secondary_occupation'].widget = ListTextWidget(data_list=secondary_occupation_list, name='secondary_occupation-list')
        tertiary_occupation_list = Occupation.objects.values_list('occupation')
        self.fields['tertiary_occupation'].widget = ListTextWidget(data_list=tertiary_occupation_list, name='tertiary_occupation-list')
        place_of_work_list = PlaceOfWork.objects.values_list('place')
        self.fields['place_of_work'].widget = ListTextWidget(data_list=place_of_work_list, name='place_of_work-list')
        literacy_status_list = LiteracyStatus.objects.values_list('status')
        self.fields['literacy_status'].widget = ListTextWidget(data_list=literacy_status_list, name='literacy_status-list')
        education_level_list = Education.objects.values_list('level')
        self.fields['education_level'].widget = ListTextWidget(data_list=education_level_list,name='education_level-list')




