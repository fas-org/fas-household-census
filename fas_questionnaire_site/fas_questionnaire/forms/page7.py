from django import forms
from ..models.page7 import InputUseSeeds,InputUseFertiliser,InputUseManure,InputUsePlantProtectionIrrigation
from django.forms.models import model_to_dict, fields_for_model


class InputUseForm(forms.Form):
    #fields corresponding to InputUseManure Model
    crop_code = forms.CharField(max_length=30)
    manure_type = forms.CharField(max_length=30)
    manure_home_qunatity = forms.CharField(max_length=30)
    manure_home_unit = forms.CharField(max_length=30)
    manure_home_value = forms.CharField(max_length=30)
    manure_purchased_quantity = forms.CharField(max_length=30)
    manure_purchased_unit = forms.CharField(max_length=30)
    manure_purchase_price = forms.CharField(max_length=30)

    #fields corresponding to InputUsePlantProtectionIrrigation
    plant_protection_quantity = forms.CharField(max_length=50)  # This field type is a guess.
    plant_protection_price = forms.CharField(max_length=50)  # This field type is a guess.
    irrigation_source = forms.CharField(max_length=50)
    irrigation_price = forms.CharField(max_length=50)  # This field type is a guess.

    #fields corresponding to InputUseFertiliser
    fertiliser_type = forms.CharField(max_length=50)
    fertiliser_quantity = forms.CharField()  # This field type is a guess.
    fertiliser_price = forms.CharField()  # This field type is a guess.

    #fields corresponding to InpitUseSeeds
    home_produced_quantity = forms.CharField()  # This field type is a guess.
    home_produced_value = forms.CharField()  # This field type is a guess.
    purchased_quantity = forms.CharField()  # This field type is a guess.
    purchased_price = forms.CharField()

    class Meta:
        fields = ('plant_protection_quantity','plant_protection_price','irrigation_price','irrigation_source','crop_code', 'manure_type', 'manure_home_unit', 'manure_purchased_unit', 'manure_purchased_quantity', 'manure_home_value', 'manure_home_qunatity','manure_purchase_price','fertiliser_price','fertiliser_quantity','fertiliser_type','home_produced_quantity','home_produced_value','purchased_price','purchased_quantity')

    def save(self, *args, **kwargs):
        data = self.cleaned_data
        input_use_manure_form = InputUseManureForm(data)
        input_use_plant_protection_form = InputUsePlantProtectionIrrigationForm(data)
        input_use_fertiliser = InputUseFertiliserForm(data)
        input_use_seeds = InputUseSeedsForm(data)


class InputUseManureForm(forms.ModelForm):
    class Meta:
        model = InputUseManure
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}


class InputUsePlantProtectionIrrigationForm(forms.ModelForm):
    class Meta:
        model = InputUsePlantProtectionIrrigation
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}


class InputUseFertiliserForm(forms.ModelForm):
    class Meta:
        model = InputUseFertiliser
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}


class InputUseSeedsForm(forms.ModelForm):
    class Meta:
        model = InputUseSeeds
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}
