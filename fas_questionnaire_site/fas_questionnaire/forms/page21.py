from django import forms
from ..models.page21 import AssetOwnership,AssetType,AssetCategory


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
        self.fields['type_of_asset'].queryset = AssetType.objects.filter(asset_category_id=AssetCategory.objects.get(asset_category="Immovables").id)

