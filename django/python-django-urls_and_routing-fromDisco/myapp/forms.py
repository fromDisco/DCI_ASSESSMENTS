from django import forms

from .models import Weather


class DateInput(forms.DateInput):
    input_type = "date"


class WeatherForm(forms.ModelForm):
    class Meta:
        model = Weather
        fields = "__all__"

        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
        }
