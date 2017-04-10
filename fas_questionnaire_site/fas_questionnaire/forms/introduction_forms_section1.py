from django import forms
from ..models.introduction_models_section1 import HouseholdIntroduction


class HouseholdIntroductionForm(forms.ModelForm):
    class Meta:
        model = HouseholdIntroduction
        fields = ['household', 'sample_number', 'os_rs_reason', 'household_head_name', 'sex', 'age', 'address', 'birth_village',
                  'birth_tehsil', 'birth_district', 'year_of_migration', 'caste_tribe', 'sc_st', 'religion',
                  'father_name', 'father_occupation', 'telephone_no', 'comments']
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    # this is to remove the mandatory fields
    # def __init__(self, *args, **kwargs):
    #     super(HouseholdIntroductionForm, self).__init__(*args, **kwargs)
    #     for key in self.fields:
    #         self.fields[key].required = False

