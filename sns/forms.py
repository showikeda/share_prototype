from django import forms
# from share.sns.models import Comment


class SearchForm(forms.Form):
    keyword = forms.CharField(max_length=100)


# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = 'image'
