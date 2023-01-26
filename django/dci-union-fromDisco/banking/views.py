# import python modules 
from decimal import Decimal
from urllib import parse

# import django modules
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from django.urls import reverse, reverse_lazy
# import external modules
from forex_python.converter import CurrencyRates

# import app/project modules
from .forms import SendMoneyForm
from .helpers import get_country_name, get_country_names_currs


class SendMoneyView(FormView):
    template_name = "banking/transaction.html"
    success_template = "banking/post-transaction.html"
    form_class = SendMoneyForm

    
    def post(self, request, *args, **kwargs):
        """
        Convert form sender currency to reciever currency
        """
        request_object = request.POST
        from_country_curr = request_object.get("from_country")
        to_country_curr = request_object.get("to_country")
        # get amount of transfered money
        amount_from = request_object.get("amount_from")

        # Form responses are country currencies. 
        # Get the matching country name for the currency
        # with the actual code its not possible to get the country name
        # because only the currency is send. 
        # And, e.g. the EUR is currency in multiple countries
        # so its not possible to get the country by a given currency
        ##########################################################
        # from_country_name = get_country_name(from_country_curr)
        # to_country_name = get_country_name(to_country_curr)

        currency = CurrencyRates(force_decimal=True)
        # convert the incoming amount to the currency of recievers country
        try:
            converted = currency.convert(from_country_curr, to_country_curr, Decimal(amount_from))
        except:
            converted = "Something went wrong"

        context = {
            "converted": round(converted, 2),
            "amount": amount_from,
            "from_country_curr": from_country_curr,
            "to_country_curr": to_country_curr,
        }

        # with an logged in user the data would be stored in a session variable,
        # that could be called from the recieving function
        # request.session["converted"] = converted
        endcoded = parse.urlencode(context)
        return redirect("banking:post_transaction", data=endcoded)

    
class PostTransactionView(TemplateView):
    template_name = "banking/post-transaction.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["data"] = parse.parse_qs(kwargs.get("data"))
        return context
    