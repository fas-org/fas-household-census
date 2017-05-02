from django import forms

from fas_questionnaire.models.page2 import IrrigationSource
from fas_questionnaire.models.page5 import CroppingPatternAndCropSchedule
from ..models.page7 import InputUseSeeds, InputUseFertiliser, InputUseManure, InputUsePlantProtectionIrrigation, \
    ManureType, FertilizerType
from ..views.common import is_empty
import re


class InputUseForm(forms.Form):
    code_choices = [('', '-----')]
    crop_code = forms.ChoiceField(code_choices, required=False, widget=forms.Select())
    manure_type_choices = [('', '-----')]
    manure_type = forms.ChoiceField(manure_type_choices, required=False, widget=forms.Select())
    manure_home_quantity = forms.CharField(max_length=30, required=False)
    manure_home_unit = forms.CharField(max_length=30, required=False)
    manure_home_value = forms.CharField(max_length=30, required=False)
    manure_purchased_quantity = forms.CharField(max_length=30, required=False)
    manure_purchased_unit = forms.CharField(max_length=30, required=False)
    manure_purchased_price = forms.CharField(max_length=30, required=False)

    # fields corresponding to InputUsePlantProtectionIrrigation
    plant_protection_quantity = forms.FloatField(required=False)
    plant_protection_price = forms.FloatField(required=False)
    irrigation_choices = [('', '-----')]
    irrigation_source = forms.ChoiceField(irrigation_choices, required=False, widget=forms.Select())
    irrigation_price = forms.FloatField(required=False)

    # fields corresponding to InputUseFertiliser
    fertilizer_type_coices = [('', '-----')]
    fertiliser_type = forms.ChoiceField(fertilizer_type_coices, required=False, widget=forms.Select())
    fertiliser_quantity = forms.FloatField(required=False)
    fertiliser_price = forms.FloatField(required=False)

    # fields corresponding to InputUseSeeds
    home_produced_quantity = forms.FloatField(required=False)
    home_produced_value = forms.CharField(max_length=50, required=False)
    purchased_quantity = forms.FloatField(required=False)
    purchased_price = forms.FloatField(required=False)

    class Meta:
        fields = (
            'plant_protection_quantity', 'plant_protection_price', 'irrigation_price', 'irrigation_source', 'crop_code',
            'manure_type', 'manure_home_unit', 'manure_purchased_unit', 'manure_purchased_quantity',
            'manure_home_value',
            'manure_home_qunatity', 'manure_purchase_price', 'fertiliser_price', 'fertiliser_quantity',
            'fertiliser_type',
            'home_produced_quantity', 'home_produced_value', 'purchased_price', 'purchased_quantity')

    def __init__(self, *args, **kwargs):
        super(InputUseForm, self).__init__(*args, **kwargs)

        crop_code_query = CroppingPatternAndCropSchedule.objects.values_list('serial_no', flat=True).distinct()
        manure_type_query = ManureType.objects.values_list('type', flat=True).distinct()
        fertilizer_type_query = FertilizerType.objects.values_list('type', flat=True).distinct()
        irrigation_source_query = IrrigationSource.objects.values_list('source', flat=True).distinct()

        code_choices = [('', '-----')] + [(region, region) for region in crop_code_query]
        manure_type_choices = [('', '-----')] + [(region, region) for region in manure_type_query]
        fertiliser_type_choices = [('', '-----')] + [(region, region) for region in fertilizer_type_query]
        irrigation_source_choices = [('', '-----')] + [(region, region) for region in irrigation_source_query]

        self.fields["crop_code"].choices = code_choices
        self.fields["manure_type"].choices = manure_type_choices
        self.fields["fertiliser_type"].choices = fertiliser_type_choices
        self.fields["irrigation_source"].choices = irrigation_source_choices

    def save(self, household_id, *args, **kwargs):
        data = self.cleaned_data
        request_ids = [args[0][x] for x in args[0] if re.search('-crop_code', x) and args[0][x] != ""]
        if not is_empty(request_ids):
            InputUseManure.objects.exclude(crop_code__in=request_ids).delete()
            InputUsePlantProtectionIrrigation.objects.exclude(crop_code__in=request_ids).delete()
            InputUseFertiliser.objects.exclude(crop_code__in=request_ids).delete()
            InputUseSeeds.objects.exclude(crop_code__in=request_ids).delete()

        input_use_manure_form = InputUseManureForm(data)
        input_use_plant_protection_form = InputUsePlantProtectionIrrigationForm(data)
        input_use_fertiliser = InputUseFertiliserForm(data)
        input_use_seeds = InputUseSeedsForm(data)

        from fas_questionnaire.views.page7 import save_page7_form
        return save_page7_form(input_use_manure_form, household_id, InputUseManure) and save_page7_form(
            input_use_plant_protection_form, household_id, InputUsePlantProtectionIrrigation) \
               and save_page7_form(input_use_fertiliser, household_id, InputUseFertiliser) and save_page7_form(
            input_use_seeds, household_id, InputUseSeeds)


class InputUseManureForm(forms.ModelForm):
    class Meta:
        model = InputUseManure
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def is_valid(self):
        for (key, value) in self.base_fields.items():
            if not is_empty(self[key]) and not key == 'crop_code':
                return True
        return False


class InputUsePlantProtectionIrrigationForm(forms.ModelForm):
    class Meta:
        model = InputUsePlantProtectionIrrigation
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def is_valid(self):
        for (key, value) in self.base_fields.items():
            if not is_empty(self[key]) and not key == 'crop_code':
                return True
        return False


class InputUseFertiliserForm(forms.ModelForm):
    class Meta:
        model = InputUseFertiliser
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def is_valid(self):
        for (key, value) in self.base_fields.items():
            if not is_empty(self[key]) and not key == 'crop_code':
                return True
        return False


class InputUseSeedsForm(forms.ModelForm):
    class Meta:
        model = InputUseSeeds
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def is_valid(self):
        for (key, value) in self.base_fields.items():
            if not is_empty(self[key]) and not key == 'crop_code':
                return True
        return False
