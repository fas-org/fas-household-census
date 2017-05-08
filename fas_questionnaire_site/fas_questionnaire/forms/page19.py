from django import forms
from ..models.page19 import PublicDistributionSystem, WaterForDomesticUse, Housing, HousingComments


class PublicDistributionSystemForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = PublicDistributionSystem
        exclude = ['household']


class WaterForDomesticUseForm(forms.ModelForm):
    class Meta:
        model = WaterForDomesticUse
        exclude = ['household']


class HousingForm(forms.ModelForm):
    class Meta:
        model = Housing
        exclude = ['household']


class HousingCommentsForm(forms.ModelForm):
    id=forms.CharField(widget=forms.HiddenInput(),required=False)
    class Meta:
        model = HousingComments
        exclude = ['household']
        widgets = {
            'comments' : forms.Textarea(attrs={'width':'100%', 'rows':'3'})
        }
