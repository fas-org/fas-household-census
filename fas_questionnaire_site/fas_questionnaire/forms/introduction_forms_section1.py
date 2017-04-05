from django import forms
from ..models.introduction_models_section1 import HouseholdIntroduction


class HouseholdIntroductionForm(forms.ModelForm):
    class Meta:
        model = HouseholdIntroduction
        fields = ['household', 'household_head_name', 'sex', 'age', 'caste_tribe', 'religion', 'birth_village_tehsil',
                  'year_of_migration', 'father_name', 'father_occupation', 'address', 'telephone_no']
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    # this is to remove the mandatory fields
    def __init__(self, *args, **kwargs):
        super(HouseholdIntroductionForm, self).__init__(*args, **kwargs)
        for key in self.fields:
            self.fields[key].required = False

