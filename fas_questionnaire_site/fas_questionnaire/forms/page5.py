from django import forms

from fas_questionnaire.forms.common import ListTextWidget
from ..models.page5 import *


class CroppingPatternAndCropScheduleForm(forms.ModelForm):
    class Meta:
        model = CroppingPatternAndCropSchedule
        fields = ['household',
                  'crop_number_first_digit',
                  'crop_number_second_digit',
                  'id',
                  'crop',
                  'variety',
                  'tenurial_status',
                  'crop_homestead_land',
                  'extent',
                  'month_of_sowing',
                  'month_of_harvesting',
                  'source_of_irrigation',
                  'comments',
                  ]
        exclude = ['household']
        widgets = None
        labels = {}
        localized_fields = None
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        super(CroppingPatternAndCropScheduleForm, self).__init__(*args, **kwargs)
        crops_list = Crop.objects.values_list('name')
        self.fields['crop'].widget = ListTextWidget(data_list=crops_list, name='cropping-list')
        tenurial_status_list = Tenurial.objects.values_list('status')
        self.fields['tenurial_status'].widget = ListTextWidget(data_list=tenurial_status_list, name='tenurial_status_pattern-list')
        crop_homestead_land_list = HomesteadLand.objects.values_list('land_name')
        self.fields['crop_homestead_land'].widget = ListTextWidget(data_list=crop_homestead_land_list, name='cropping_crop_homestead_land-list')
        month_of_sowing_list = Month.objects.values_list('month')
        self.fields['month_of_sowing'].widget = ListTextWidget(data_list=month_of_sowing_list, name='cropping_month_of_sowing-list')
        month_of_harvesting_list = Month.objects.values_list('month')
        self.fields['month_of_harvesting'].widget = ListTextWidget(data_list=month_of_harvesting_list, name='cropping_month_of_harvesting-list')
        source_of_irrigation_list = IrrigationSource.objects.values_list('source')
        self.fields['source_of_irrigation'].widget = ListTextWidget(data_list=source_of_irrigation_list, name='cropping_source_of_irrigation-list')

