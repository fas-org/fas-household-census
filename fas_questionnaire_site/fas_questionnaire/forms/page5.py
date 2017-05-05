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


class CroppingPatternAndCropScheduleCommentsForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = CroppingPatternAndCropScheduleComments
        fields = ['household', 'comments_notes', 'id']
        exclude = ['household']
        widgets = {
            'comments_notes': forms.Textarea(attrs={'rows': 10, 'cols': 198})
        }
        localized_fields = None
        help_texts = {}
        error_messages = {}
