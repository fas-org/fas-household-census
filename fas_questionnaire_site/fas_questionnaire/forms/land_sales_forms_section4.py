from django import forms
from ..models.land_sales_models_section4 import LandPurchased, LandSold, LandPurchasedComments


class LandPurchasedForm(forms.ModelForm):
    class Meta:
        model = LandPurchased
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}


class LandSoldForm(forms.ModelForm):
    class Meta:
        model = LandSold
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
