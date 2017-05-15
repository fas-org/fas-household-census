from django import forms

from fas_questionnaire.forms.common import ListTextWidget
from fas_questionnaire.models.common import YesOrNo
from ..models.page18 import *


class AcquisitionAndLossOfMajorAssetsForm(forms.ModelForm):
    class Meta:
        model = AcquisitionAndLossOfMajorAssets
        exclude = ['household']
        widgets = None
        localized_fields = None
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        super(AcquisitionAndLossOfMajorAssetsForm, self).__init__(*args, **kwargs)
        assets_list = DescriptionOfAssets.objects.values_list('asset_name')
        self.fields['description_of_asset'].widget = ListTextWidget(data_list=assets_list, name='assets-list')

        month_list = Month.objects.values_list('month')
        self.fields['month_of_sale'].widget = ListTextWidget(data_list=month_list, name='month_list')

        month_list = Month.objects.values_list('month')
        self.fields['month_of_purchase'].widget = ListTextWidget(data_list=month_list, name='month_list')

class ForChildrenOfAge616YearsForm(forms.ModelForm):
    class Meta:
        model = ForChildrenOfAge616Years
        exclude = ['household']
        widgets = None
        localized_fields = None
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        super(ForChildrenOfAge616YearsForm, self).__init__(*args, **kwargs)

        whether_enrolled_in_eductional_institution_currently_list = YesOrNo.objects.values_list('title')
        self.fields['whether_enrolled_in_eductional_institution_currently'].widget = ListTextWidget(data_list=whether_enrolled_in_eductional_institution_currently_list, name='whether_enrolled_in_eductional_institution_currently_list')

        whether_ever_enrolled_in_school_list = YesOrNo.objects.values_list('title')
        self.fields['whether_ever_enrolled_in_school'].widget = ListTextWidget(data_list=whether_ever_enrolled_in_school_list,name='whether_ever_enrolled_in_school_list')
