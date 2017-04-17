from django import forms
from ..models.page1 import HouseholdIntroduction, HouseholdMembers


class HouseholdIntroductionForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = HouseholdIntroduction
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}


class HouseholdMembersForm(forms.ModelForm):
    class Meta:
        model = HouseholdMembers
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}
