from django import forms
from ..models.page15 import *


class LongTermWorkersForm(forms.ModelForm):
    class Meta:
        model = LongTermWorkers
        fields = ['household', 'worker_name', 'employer_name', 'residence_village', 'caste', 'occupation', 'land_owned',
                  'land_leased_in', 'land_leased_out', 'agricultural_labor', 'operating_machines', 'tending_animals',
                  'non_agri_business', 'domestic_work', 'other_activities', 'months_employed', 'earning_cash',
                  'earning_kind', 'comments']
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}
