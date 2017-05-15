from django import forms

from fas_questionnaire.forms.common import ListTextWidget
from fas_questionnaire.models.common import Crop
from ..models.page11 import *


class LabourDaysEmployedInAgriculturalOperationsForm(forms.ModelForm):

    class Meta:
        model = LabourDaysEmployedInAgriculturalOperations
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        super(LabourDaysEmployedInAgriculturalOperationsForm, self).__init__(*args, **kwargs)
        crop_list = Crop.objects.values_list('name')
        self.fields['crop'].widget = ListTextWidget(data_list=crop_list, name='crop_list')