from django import forms
from ..models.land_sales_models_section4 import LandPurchased, LandSold


class LandPurchasedForm(forms.ModelForm):
    class Meta:
        model = LandPurchased
        fields = ['household', 'year_of_purchase', 'extent_of_land_bought',
                  'type_of_land_purchased', 'name_of_seller',
                  'caste_of_seller', 'occupation_of_seller',
                  'place_of_residence_of_seller', 'price_of_land_purchased',
                  'comments']
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {
            'extent_of_land_bought': 'Extent',
            'type_of_land_purchased': 'Type of Land',
            'name_of_seller': 'Name',
            'caste_of_seller': 'Caste',
            'occupation_of_seller': 'Occupation',
            'place_of_residence_of_seller': 'Place of residence',
            'price_of_land_purchased': 'price of land'
        }
        help_texts = {}
        error_messages = {}


class LandSoldForm(forms.ModelForm):
    class Meta:
        model = LandSold
        fields = ['household', 'year_of_sale', 'extent_of_land_sold',
                  'type_of_land_sold', 'name_of_buyer', 'caste_of_buyer',
                  'occupation_of_buyer', 'place_of_residence_of_buyer',
                  'price_of_land_sold', 'reasons_for_sale']
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {
            'extent_of_land_sold': 'Extent',
            'type_of_land_sold': 'Type of Land',
            'name_of_buyer': 'Name',
            'caste_of_buyer': 'Caste',
            'occupation_of_buyer': 'Occupation',
            'place_of_residence_of_buyer': 'Place of residence',
            'price_of_land_sold': 'Price of land',

        }
        help_texts = {}
        error_messages = {}
