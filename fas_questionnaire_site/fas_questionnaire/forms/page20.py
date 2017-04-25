from django import forms
from ..models.page20 import *


class OutstandingLoansForm(forms.ModelForm):

    class Meta:
        model = OutstandingLoans
        exclude = ['household_number']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

class LoansBorrowedLastYearAndRepaidForm(forms.ModelForm):

    class Meta:
        model = LoansBorrowedLastYearAndRepaid
        exclude = ['household_number']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

class MembershipInSelfHelpGroupsForm(forms.ModelForm):

    class Meta:
        model = MembershipInSelfHelpGroups
        exclude = ['household_number']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

class DetailsOfBankPostofficeAccountOfTheHouseholdForm(forms.ModelForm):

    class Meta:
        model = DetailsOfBankPostofficeAccountOfTheHousehold
        exclude = ['household_number']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}
