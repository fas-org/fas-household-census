from django import forms
from .models import Household


class HouseholdForm(forms.ModelForm):

    class Meta:
        model = Household
        fields = ['head_name', 'sex', 'caste', 'religion', 'birth_village', 'father_name', 'father_occupation', 'telephone']
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

