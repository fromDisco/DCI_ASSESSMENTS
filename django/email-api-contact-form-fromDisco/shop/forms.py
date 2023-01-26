# import the forms module

from django import forms
from django.core.exceptions import ValidationError
from better_profanity import profanity
# inherit from forms.Form

# organization
CAR_CHOICES = (
    ('bmw', "BMW"),
    ('tesla', "Tesla"),
    ('fiat', "Fiat"),
    ('audi', "Audi"),
)

def validate_email(value):
    val_list = value.split(".")
    if "kp" in val_list:
        raise ValidationError("No valid mail")

def validate_words(value):
    if profanity.contains_profanity(value):
        raise ValidationError("You should learn some good manners.")

class CarSearch(forms.Form):
    start_date = forms.DateField(label='When do you want to take car?', widget=forms.SelectDateWidget)
    end_date = forms.DateField(label='when to bring back car?', widget=forms.SelectDateWidget)
    cars = forms.CharField(initial="fiat", label="Choose your car", widget=forms.Select(choices=CAR_CHOICES), help_text="All our cars are premium, if you scratch you pay!")


class SearchForm(forms.Form):
    # TODO: add date support e.g. when money should arrive to the person you are sending it to.
    search_term = forms.DateField(label='What is your birth date?', widget=forms.SelectDateWidget)

class HotelSearch(forms.Form):    
    start_date = forms.DateField(label='Checkin', widget=forms.SelectDateWidget)
    end_date = forms.DateField(label='Checkout', widget=forms.SelectDateWidget)


class ContactForm(forms.Form):
    name = forms.CharField(max_length=30, required=False, validators=[validate_words])
    email = forms.EmailField(validators=[validate_email]) # some validations in frontend
    reason = forms.CharField(widget=forms.Textarea, validators=[validate_words])