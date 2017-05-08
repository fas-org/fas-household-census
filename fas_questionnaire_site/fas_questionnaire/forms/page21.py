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
                  'value_of_assets',
                  'comments']
        exclude = ['household', 'asset_group']
        localized_fields = None
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        super(ImmovableForm, self).__init__(*args, **kwargs)
        self.fields['type_of_asset'].queryset = AssetType.objects.filter(
            asset_category_id=AssetCategory.objects.get(asset_category="Immovables").id)

    def clean(self):
        return clean(self)


class MeansOfTransportForm(forms.ModelForm):
    class Meta:
        model = AssetOwnership
        fields = ['id',
                  'household',
                  'type_of_asset',
                  'asset_group',
                  'number_of_assets_owned',
                  'value_of_assets',
                  'comments']
        exclude = ['household', 'asset_group']
        localized_fields = None
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        super(MeansOfTransportForm, self).__init__(*args, **kwargs)
        self.fields['type_of_asset'].queryset = AssetType.objects.filter(
            asset_category_id=AssetCategory.objects.get(asset_category="MeansOfTransport").id)

    def clean(self):
        return clean(self)


class FurnitureForm(forms.ModelForm):
    class Meta:
        model = AssetOwnership
        fields = ['id',
                  'household',
                  'type_of_asset',
                  'asset_group',
                  'number_of_assets_owned',
                  'value_of_assets',
                  'comments']
        exclude = ['household', 'asset_group']
        localized_fields = None
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        super(FurnitureForm, self).__init__(*args, **kwargs)
        self.fields['type_of_asset'].queryset = AssetType.objects.filter(
            asset_category_id=AssetCategory.objects.get(asset_category="Furniture").id)

    def clean(self):
        return clean(self)


class ElectricEquipmentsForm(forms.ModelForm):
    class Meta:
        model = AssetOwnership
        fields = ['id',
                  'household',
                  'type_of_asset',
                  'asset_group',
                  'number_of_assets_owned',
                  'value_of_assets',
                  'comments']
        exclude = ['household', 'asset_group']
        localized_fields = None
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        super(ElectricEquipmentsForm, self).__init__(*args, **kwargs)
        self.fields['type_of_asset'].queryset = AssetType.objects.filter(
            asset_category_id=AssetCategory.objects.get(asset_category="ElectricEquipments").id)

    def clean(self):
        return clean(self)


class OtherDomesticDurableGoodsForm(forms.ModelForm):
    class Meta:
        model = AssetOwnership
        fields = ['id',
                  'household',
                  'type_of_asset',
                  'asset_group',
                  'number_of_assets_owned',
                  'value_of_assets',
                  'comments']
        exclude = ['household', 'asset_group']
        localized_fields = None
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        super(OtherDomesticDurableGoodsForm, self).__init__(*args, **kwargs)
        self.fields['type_of_asset'].queryset = AssetType.objects.filter(
            asset_category_id=AssetCategory.objects.get(asset_category="OtherDomesticDurableGoods").id)

    def clean(self):
        return clean(self)


class InventoriesForm(forms.ModelForm):
    class Meta:
        model = AssetOwnership
        fields = ['id',
                  'household',
                  'type_of_asset',
                  'asset_group',
                  'number_of_assets_owned',
                  'value_of_assets',
                  'comments']
        exclude = ['household', 'asset_group']
        localized_fields = None
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        super(InventoriesForm, self).__init__(*args, **kwargs)
        self.fields['type_of_asset'].queryset = AssetType.objects.filter(
            asset_category_id=AssetCategory.objects.get(asset_category="Inventories").id)

    def clean(self):
        return clean(self)


class MiscellaneousForm(forms.ModelForm):
    class Meta:
        model = AssetOwnership
        fields = ['id',
                  'household',
                  'type_of_asset',
                  'asset_group',
                  'number_of_assets_owned',
                  'value_of_assets',
                  'comments']
        exclude = ['household', 'asset_group']
        localized_fields = None
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        super(MiscellaneousForm, self).__init__(*args, **kwargs)
        self.fields['type_of_asset'].queryset = AssetType.objects.filter(
            asset_category_id=AssetCategory.objects.get(asset_category="Miscellaneous").id)

    def clean(self):
        return clean(self)


class AssetLandRegistrationForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = AssetLandRegistration
        fields = ['id', 'household', 'land_registered_details', 'comments']
        exclude = ['household']
        widgets = {
            'land_registered_details': forms.Textarea(attrs={'rows': 3, 'width': '100%'})
        }
        localized_fields = None
        help_texts = {}
        error_messages = {}


def clean(form):
    for param in form.cleaned_data:
        from fas_questionnaire.views.common import is_empty
        if not param == 'type_of_asset' and not is_empty(form.cleaned_data[param]):
            if form.cleaned_data['type_of_asset'] is None:
                raise forms.ValidationError('Asset Type is mandatory for entering other details in the record')
    return form.cleaned_data
