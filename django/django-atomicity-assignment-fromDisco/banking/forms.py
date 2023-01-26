from django import forms

from .models import Customer, Transaction


class NewCustomerForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    amount = forms.DecimalField(decimal_places=2, min_value=0.00)
    # joining_date = forms.DateField()


class TransactionForm(forms.Form):
    sender = forms.CharField(widget=forms.TextInput(attrs={"readonly": "readonly"}))
    reciever = forms.CharField()
    amount = forms.DecimalField(decimal_places=2, min_value=0.00)
