from django import forms
from ..models.common import Comments


class CommentsForm(forms.ModelForm):

    class Meta:
        model = Comments
        exclude = ['household']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}