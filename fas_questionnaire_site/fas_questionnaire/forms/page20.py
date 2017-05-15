from django import forms

from fas_questionnaire.forms.common import ListTextWidget
from fas_questionnaire.models.common import Month
from ..models.page20 import *


class OutstandingLoansForm(forms.ModelForm):

    class Meta:
        model = OutstandingLoans
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        super(OutstandingLoansForm, self).__init__(*args, **kwargs)
        source_of_borrowing_list = SourceOfBorrowing.objects.values_list('source_of_borrowing')
        self.fields['source_of_borrowing'].widget = ListTextWidget(data_list=source_of_borrowing_list, name='source_of_borrowing-list')
        purpose_of_borrowing_list = PurposeOfBorrowing.objects.values_list('purpose_of_borrowing')
        self.fields['purpose_of_borrowing'].widget = ListTextWidget(data_list=purpose_of_borrowing_list, name='purpose_of_borrowing-list')


class LoansBorrowedLastYearAndRepaidForm(forms.ModelForm):

    class Meta:
        model = LoansBorrowedLastYearAndRepaid
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        super(LoansBorrowedLastYearAndRepaidForm, self).__init__(*args, **kwargs)
        month_when_fully_repaid_list = Month.objects.values_list('month')
        self.fields['month_when_fully_repaid'].widget = ListTextWidget(data_list=month_when_fully_repaid_list, name='month_when_fully_repaid-list')
        source_of_borrowing_list = SourceOfBorrowing.objects.values_list('source_of_borrowing')
        self.fields['source_of_borrowing'].widget = ListTextWidget(data_list=source_of_borrowing_list, name='source_of_borrowing-list')
        purpose_of_borrowing_list = PurposeOfBorrowing.objects.values_list('purpose_of_borrowing')
        self.fields['purpose_of_borrowing'].widget = ListTextWidget(data_list=purpose_of_borrowing_list, name='purpose_of_borrowing-list')




class MembershipInSelfHelpGroupsForm(forms.ModelForm):

    class Meta:
        model = MembershipInSelfHelpGroups
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        super(MembershipInSelfHelpGroupsForm, self).__init__(*args, **kwargs)
        bank_ngo_to_which_the_group_is_linked_list = BankNgoToWhichTheGroupIsLinked.objects.values_list('bank_ngo_to_which_the_group_is_linked')
        self.fields['bank_ngo_to_which_the_group_is_linked'].widget = ListTextWidget(data_list=bank_ngo_to_which_the_group_is_linked_list, name='bank_ngo_to_which_the_group_is_linked-list')
        period_of_membership_list = PeriodOfMembership.objects.values_list('period_of_membership')
        self.fields['period_of_membership'].widget = ListTextWidget(data_list=period_of_membership_list, name='period_of_membership-list')


class DetailsOfBankPostofficeAccountOfTheHouseholdForm(forms.ModelForm):

    class Meta:
        model = DetailsOfBankPostofficeAccountOfTheHousehold
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        super(DetailsOfBankPostofficeAccountOfTheHouseholdForm, self).__init__(*args, **kwargs)
        name_of_bank_post_office_list = NameOfBankPostOffice.objects.values_list('name_of_bank_post_office')
        self.fields['name_of_bank_post_office'].widget = ListTextWidget(data_list=name_of_bank_post_office_list, name='name_of_bank_post_office-list')
        type_of_account_list = TypeOfAccount.objects.values_list('type_of_account')
        self.fields['type_of_account'].widget = ListTextWidget(data_list=type_of_account_list, name='type_of_account-list')
