from django import forms
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