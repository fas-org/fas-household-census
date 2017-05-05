from django import forms
from ..models.page21 import AssetOwnership, AssetType, AssetCategory, AssetLandRegistration


class ImmovableForm(forms.ModelForm):
    class Meta:
        model = AssetOwnership
        fields = ['id',
                  'household',
                  'type_of_asset',
                  'asset_group',
                  'number_of_assets_owned',
                  'value_of_assets']
        exclude = ['household', 'asset_group']
        localized_fields = None
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        super(ImmovableForm, self).__init__(*args, **kwargs)
        self.fields['type_of_asset'].queryset = AssetType.objects.filter(
            asset_category_id=AssetCategory.objects.get(asset_category="Immovables").id)


class MeansOfTransportForm(forms.ModelForm):
    class Meta:
        model = AssetOwnership
        fields = ['id',
                  'household',
                  'type_of_asset',
                  'asset_group',
                  'number_of_assets_owned',
                  'value_of_assets']
        exclude = ['household', 'asset_group']
        localized_fields = None
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        super(MeansOfTransportForm, self).__init__(*args, **kwargs)
        self.fields['type_of_asset'].queryset = AssetType.objects.filter(
            asset_category_id=AssetCategory.objects.get(asset_category="MeansOfTransport").id)


class FurnitureForm(forms.ModelForm):
    class Meta:
        model = AssetOwnership
        fields = ['id',
                  'household',
                  'type_of_asset',
                  'asset_group',
                  'number_of_assets_owned',
                  'value_of_assets']
        exclude = ['household', 'asset_group']
        localized_fields = None
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        super(FurnitureForm, self).__init__(*args, **kwargs)
        self.fields['type_of_asset'].queryset = AssetType.objects.filter(
            asset_category_id=AssetCategory.objects.get(asset_category="Furniture").id)


class ElectricEquipmentsForm(forms.ModelForm):
    class Meta:
        model = AssetOwnership
        fields = ['id',
                  'household',
                  'type_of_asset',
                  'asset_group',
                  'number_of_assets_owned',
                  'value_of_assets']
        exclude = ['household', 'asset_group']
        localized_fields = None
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        super(ElectricEquipmentsForm, self).__init__(*args, **kwargs)
        self.fields['type_of_asset'].queryset = AssetType.objects.filter(
            asset_category_id=AssetCategory.objects.get(asset_category="ElectricEquipments").id)


class OtherDomesticDurableGoodsForm(forms.ModelForm):
    class Meta:
        model = AssetOwnership
        fields = ['id',
                  'household',
                  'type_of_asset',
                  'asset_group',
                  'number_of_assets_owned',
                  'value_of_assets']
        exclude = ['household', 'asset_group']
        localized_fields = None
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        super(OtherDomesticDurableGoodsForm, self).__init__(*args, **kwargs)
        self.fields['type_of_asset'].queryset = AssetType.objects.filter(
            asset_category_id=AssetCategory.objects.get(asset_category="OtherDomesticDurableGoods").id)


class InventoriesForm(forms.ModelForm):
    class Meta:
        model = AssetOwnership
        fields = ['id',
                  'household',
                  'type_of_asset',
                  'asset_group',
                  'number_of_assets_owned',
                  'value_of_assets']
        exclude = ['household', 'asset_group']
        localized_fields = None
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        super(InventoriesForm, self).__init__(*args, **kwargs)
        self.fields['type_of_asset'].queryset = AssetType.objects.filter(
            asset_category_id=AssetCategory.objects.get(asset_category="Inventories").id)


class MiscellaneousForm(forms.ModelForm):
    class Meta:
        model = AssetOwnership
        fields = ['id',
                  'household',
                  'type_of_asset',
                  'asset_group',
                  'number_of_assets_owned',
                  'value_of_assets']
        exclude = ['household', 'asset_group']
        localized_fields = None
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        super(MiscellaneousForm, self).__init__(*args, **kwargs)
        self.fields['type_of_asset'].queryset = AssetType.objects.filter(
            asset_category_id=AssetCategory.objects.get(asset_category="Miscellaneous").id)


class AssetLandRegistrationForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = AssetLandRegistration
        fields = ['id', 'household', 'land_registered_details']
        exclude = ['household']
        widgets = {
            'land_registered_details': forms.Textarea(attrs={'rows': 10, 'cols': 198})
        }
        localized_fields = None
        help_texts = {}
        error_messages = {}
