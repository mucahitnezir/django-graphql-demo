from django import forms

from book.models import Country


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = 'name',
