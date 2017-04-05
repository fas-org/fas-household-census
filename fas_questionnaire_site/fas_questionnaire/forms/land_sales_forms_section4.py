from django import forms
from ..models.land_sales_models_section4 import LandBought, LandSold, Buyer, Seller


class BuyerForm(forms.ModelForm):
    class Meta:
        model = Buyer
        fields = ['name', 'caste', 'occupations', 'place_of_residence']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}


class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ['name', 'caste', 'occupations', 'place_of_residence']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}


class LandBoughtForm(forms.ModelForm):
    class Meta:
        model = LandBought
        fields = ['household', 'year_of_purchase', 'extent', 'type_of_land', 'seller', 'price_of_land', 'comments']
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}


class LandSoldForm(forms.ModelForm):
    class Meta:
        model = LandSold
        fields = ['household', 'year_of_sale', 'extent', 'type_of_land', 'buyer', 'price_of_land', 'reasons_for_sale']
        exclude = ['household', 'buyer']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}
