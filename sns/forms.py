from django import forms

from .models import Comment


# from share.sns.models import Comment


class SearchForm(forms.Form):
    keyword = forms.CharField(max_length=100)


class CommentForm(forms.ModelForm):
    file = forms.FileField(
        label=''
    )

    class Meta:
        model = Comment
        fields = ('text', 'file')


# class ImageForm(forms.ModelForm):
#     class Meta:
#         model = Image
#         fields = 'image'
