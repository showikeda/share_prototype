from django import forms

class SearchForm(forms.Form):
    keyword = forms.CharField(lable='検索', max_length=100)