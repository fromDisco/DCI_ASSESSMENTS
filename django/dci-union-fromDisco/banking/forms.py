from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

from .helpers import get_country_names_currs

class SendMoneyForm(forms.Form):
    from_country = forms.ChoiceField(choices=get_country_names_currs())
    to_country = forms.ChoiceField(choices=get_country_names_currs())
    amount_from = forms.IntegerField(label="Send Amount")
    amount_to = forms.IntegerField(label="Reciever gets", required=False, disabled=True)