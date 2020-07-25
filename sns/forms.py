from django import forms
from .models import Comment


class SearchForm(forms.Form):
    keyword = forms.CharField(max_length=100)


class CommentForm(forms.ModelForm):
    file = forms.FileField(
        label=''
    )

    class Meta:
        model = Comment
        fields = ('text', 'image')
