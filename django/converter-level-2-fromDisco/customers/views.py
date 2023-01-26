from django.shortcuts import render, HttpResponse


# Create your views here.
def phone_validator_view(request, phone):
    """
    Check if incoming url is valid
    """
    return render(request, "customers/phone_is_valid.html", context={"phone_number": phone})