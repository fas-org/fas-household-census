from django import forms

from fas_questionnaire.forms.common import ListTextWidget
from fas_questionnaire.models.common import SupportNature, Institution
from ..models.page8 import *


class ExtensionForm(forms.ModelForm):

    class Meta:
        model = Extension
        fields = ['household', 'from_whom_advice_received', 'type_of_advice_received_description', 'comments']
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {
            'from_whom_advice_received': 'Did you receive any advice regarding cultivation of crops during the last year',
            'type_of_advice_received_description': 'If Yes, what kind of advice did you receive?'
        }
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        super(ExtensionForm, self).__init__(*args, **kwargs)

        extension_list = CultivationAdviser.objects.values_list('adviser')
        self.fields['from_whom_advice_received'].widget = ListTextWidget(data_list=extension_list, name='extension-list')


class InstitutionalSupportForm(forms.ModelForm):

    class Meta:
        model = InstitutionalSupport
        fields = ['household', 'category', 'name_of_institution', 'year_of_support','nature_of_support_or_purpose', 'comments']
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}


    def __init__(self, *args, **kwargs):
        super(InstitutionalSupportForm, self).__init__(*args, **kwargs)

        category_list = InstitutionalSupportCategory.objects.values_list('category_name')
        self.fields['category'].widget = ListTextWidget(data_list=category_list,name='category_list')

        support_nature_list = SupportNature.objects.values_list('support')
        self.fields['nature_of_support_or_purpose'].widget = ListTextWidget(data_list=support_nature_list,name='support_nature_list')

        institution_list = Institution.objects.values_list('name')
        self.fields['name_of_institution'].widget = ListTextWidget(data_list=institution_list,name='institution_list')