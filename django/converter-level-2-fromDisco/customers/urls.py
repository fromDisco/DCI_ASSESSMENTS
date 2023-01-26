from django.urls import path, register_converter
from . import views

from customers.converters import PhoneNumberConverter
register_converter(PhoneNumberConverter, "phone_num")

app_name = "customers"
urlpatterns = [
    path("phone/<phone_num:phone>/", views.phone_validator_view, name="phone_validator"),
]
