from django import forms

from fas_questionnaire.forms.common import ListTextWidget
from fas_questionnaire.models.common import YesOrNo
from ..models.page19 import PublicDistributionSystem, WaterForDomesticUse, Housing, HousingComments, TypeOfRationCard, \
    ColorOfCard, SourceOfWater, SourceOfWaterOwnership, WaterSourceDistanceFromHouse, PurposeForWhichUsed, \
    WhetherOwnedOrRented, TypeOfRoof, TypeOfWall, TypeOfFloor, Latrine, ElectricityConnection, SourceOfEnergyForCooking, \
    NatureOfDisbursement


class PublicDistributionSystemForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = PublicDistributionSystem
        exclude = ['household']

    def __init__(self, *args, **kwargs):
        super(PublicDistributionSystemForm, self).__init__(*args, **kwargs)
        type_of_card_list = TypeOfRationCard.objects.values_list('type')
        self.fields['type_of_card'].widget = ListTextWidget(data_list=type_of_card_list, name='type_of_card-list')

        color_of_card_list = ColorOfCard.objects.values_list('color')
        self.fields['color_of_card'].widget = ListTextWidget(data_list=color_of_card_list, name='color_of_card_list')

        yes_or_no_list = YesOrNo.objects.values_list('title')
        self.fields['does_family_hold_ration_card'].widget = ListTextWidget(data_list=yes_or_no_list, name='yes_or_no_list')


class WaterForDomesticUseForm(forms.ModelForm):
    class Meta:
        model = WaterForDomesticUse
        exclude = ['household']

    def __init__(self, *args, **kwargs):
        super(WaterForDomesticUseForm, self).__init__(*args, **kwargs)
        source_list = SourceOfWater.objects.values_list('source')
        self.fields['source_of_water'].widget = ListTextWidget(data_list=source_list, name='source-list')

        ownership_list = SourceOfWaterOwnership.objects.values_list('ownership')
        self.fields['ownership'].widget = ListTextWidget(data_list=ownership_list, name='ownership_list')

        distance_list = WaterSourceDistanceFromHouse.objects.values_list('distance')
        self.fields['distance'].widget = ListTextWidget(data_list=distance_list, name='distance_list')

        drinking_list = PurposeForWhichUsed.objects.values_list('purpose')
        self.fields['drinking'].widget = ListTextWidget(data_list=drinking_list, name='drinking_list')

        cooking_list = PurposeForWhichUsed.objects.values_list('purpose')
        self.fields['cooking'].widget = ListTextWidget(data_list=cooking_list, name='cooking_list')

        bathing_or_cleaning_list = PurposeForWhichUsed.objects.values_list('purpose')
        self.fields['bathing_or_cleaning'].widget = ListTextWidget(data_list=bathing_or_cleaning_list, name='bathing_or_cleaning_list')

        for_animals_list = PurposeForWhichUsed.objects.values_list('purpose')
        self.fields['for_animals'].widget = ListTextWidget(data_list=for_animals_list, name='for_animals_list')


class HousingForm(forms.ModelForm):
    class Meta:
        model = Housing
        exclude = ['household']

    def __init__(self, *args, **kwargs):
        super(HousingForm, self).__init__(*args, **kwargs)
        owned_or_rented_list = WhetherOwnedOrRented.objects.values_list('type')
        self.fields['owned_or_rented'].widget = ListTextWidget(data_list=owned_or_rented_list, name='owned_or_rented-list')

        yes_or_no_list = YesOrNo.objects.values_list('title')
        self.fields['verandah_present'].widget = ListTextWidget(data_list=yes_or_no_list, name='yes_or_no-list')

        yes_or_no_list = YesOrNo.objects.values_list('title')
        self.fields['separate_kitchen'].widget = ListTextWidget(data_list=yes_or_no_list, name='yes_or_no-list')

        roof_list = TypeOfRoof.objects.values_list('type')
        self.fields['type_of_roof'].widget = ListTextWidget(data_list=roof_list, name='roof_list')

        wall_list = TypeOfWall.objects.values_list('type')
        self.fields['type_of_wall'].widget = ListTextWidget(data_list=wall_list, name='wall_list')

        floor_list = TypeOfFloor.objects.values_list('type')
        self.fields['type_of_floor'].widget = ListTextWidget(data_list=floor_list, name='floor_list')

        latrine_list = Latrine.objects.values_list('type')
        self.fields['latrine'].widget = ListTextWidget(data_list=latrine_list, name='latrine_list')

        electricity_connection_list = ElectricityConnection.objects.values_list('type')
        self.fields['electricity'].widget = ListTextWidget(data_list=electricity_connection_list, name='electricity_connection_list')

        energy_sources_list = SourceOfEnergyForCooking.objects.values_list('source')
        self.fields['energy_for_cooking'].widget = ListTextWidget(data_list=energy_sources_list, name='energy_sources_list')

        yes_or_no_list = YesOrNo.objects.values_list('title')
        self.fields['if_provided_by_govt'].widget = ListTextWidget(data_list=yes_or_no_list, name='yes_or_no_list')

        nature_of_disbursement_list = NatureOfDisbursement.objects.values_list('nature')
        self.fields['nature_of_disbursement'].widget = ListTextWidget(data_list=nature_of_disbursement_list, name='nature_of_disbursement_list')


class HousingCommentsForm(forms.ModelForm):
    id=forms.CharField(widget=forms.HiddenInput(),required=False)
    class Meta:
        model = HousingComments
        exclude = ['household']
        widgets = {
            'comments' : forms.Textarea(attrs={'width':'100%', 'rows':'3'})
        }
