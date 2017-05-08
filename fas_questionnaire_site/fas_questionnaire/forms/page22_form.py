from django import forms
from ..models.page22 import InformationOnInvestigators


class InformationOnInvestigatorsForm(forms.ModelForm):
    class Meta:
        model = InformationOnInvestigators
        fields = ['household',
                  'name_of_investigator',
                  'date_of_interview',
                  'time_taken',
                  'data_entry_by',
                  'further_investigation',
                  'date_of_entry'
                  ]
        exclude = ['household']
        labels = {
            'name_of_investigator': 'Name of Investigator/s',
            'date_of_interview': 'Date of interview',
            'time_taken': 'Time taken for interview',
            'data_entry_by': 'Data entry by',
            'date_of_entry': 'Date of data entry',
            'further_investigation': 'Is further investigation needed?'
        }
        widgets = {
            'comments_observations':forms.Textarea(attrs={'rows':10,'cols':198})
        }
        localized_fields = None
        help_texts = {}
        error_messages = {}
