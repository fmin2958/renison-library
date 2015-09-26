from django import forms

class SearchForm(forms.form):
    text = forms.CharField(label='keyword'), max_length=128)
    
