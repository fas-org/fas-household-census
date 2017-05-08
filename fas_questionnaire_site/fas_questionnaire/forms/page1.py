from django import forms

from fas_questionnaire.forms.common import ListTextWidget
from fas_questionnaire.models.common import Caste
from ..models.page1 import HouseholdIntroduction, HouseholdMembers


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


class HouseholdMembersForm(forms.ModelForm):
    class Meta:
        model = HouseholdMembers
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}
