from django import forms
from ..models.land_sales_models_section4 import LandPurchased, LandSold, LandPurchasedComments


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
        labels = {}
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
        labels = {}
        help_texts = {}
        error_messages = {}


class LandPurchasedCommentsForm(forms.ModelForm):
    class Meta:
        model = LandPurchasedComments
        fields = ['household', 'landpurchased_comments']
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}
