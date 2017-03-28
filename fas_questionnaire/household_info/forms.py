from django import forms
from .models import Household, HouseholdMembers


class HouseholdForm(forms.ModelForm):

    class Meta:
        model = Household
        fields = ['Household_number', 'head_name', 'sex', 'age', 'caste', 'religion', 'birth_village', 'year_of_migration', 'father_name', 'father_occupation', 'address', 'telephone']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(HouseholdForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(HouseholdForm, self).is_valid()

    def full_clean(self):
        return super(HouseholdForm, self).full_clean()

    def clean_head_name(self):
        head_name = self.cleaned_data.get("head_name", None)
        return head_name

    def clean_sex(self):
        sex = self.cleaned_data.get("sex", None)
        return sex

    def clean_caste(self):
        caste = self.cleaned_data.get("caste", None)
        return caste

    def clean_religion(self):
        religion = self.cleaned_data.get("religion", None)
        return religion

    def clean_birth_village(self):
        birth_village = self.cleaned_data.get("birth_village", None)
        return birth_village

    def clean_father_name(self):
        father_name = self.cleaned_data.get("father_name", None)
        return father_name

    def clean_father_occupation(self):
        father_occupation = self.cleaned_data.get("father_occupation", None)
        return father_occupation

    def clean_telephone(self):
        telephone = self.cleaned_data.get("telephone", None)
        return telephone

    def clean(self):
        return super(HouseholdForm, self).clean()

    def validate_unique(self):
        return super(HouseholdForm, self).validate_unique()

    def save(self, commit=True):
        return super(HouseholdForm, self).save(commit)


class HouseholdMembersForm(forms.ModelForm):

    class Meta:
        model = HouseholdMembers
        fields = ['Household_number', 'name', 'sex', 'age', 'relationship', 'marital_status', 'occupation', 'place_of_work', 'literacy_status', 'education_level', 'enrolled_institution']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(HouseholdMembersForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(HouseholdMembersForm, self).is_valid()

    def full_clean(self):
        return super(HouseholdMembersForm, self).full_clean()

    def clean(self):
        return super(HouseholdMembersForm, self).clean()

    def validate_unique(self):
        return super(HouseholdMembersForm, self).validate_unique()

    def save(self, commit=True):
        return super(HouseholdMembersForm, self).save(commit)