from django import forms
from ..models.householdmembers import HouseholdMembers


class HouseholdMembersForm(forms.ModelForm):
    class Meta:
        model = HouseholdMembers
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}
