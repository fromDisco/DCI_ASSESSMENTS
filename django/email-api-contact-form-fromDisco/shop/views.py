from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, FormView
from django.views.generic.edit import FormView
from django.http import HttpResponse
from django.urls import reverse_lazy
import datetime
from .forms import SearchForm, HotelSearch, CarSearch, ContactForm
from django.core.mail import send_mail

# class Browse(FormView):
#     template_name = "shop/index.html"
#     form_class = SearchForm

#     # customize initial values
#     def get_initial(self):

#         return {"search_term": "Another title"}


# Original Code
# class Browse(TemplateView):
#     template_name = "shop/index.html"
#     def get_context_data(self, *args, **kwargs):
#         return {
#             "form": SearchForm(),
#             "hotel": HotelSearch(),
#             "car": CarSearch(),
#             "contact": ContactForm()
#         }

# ALso on slack!!!# Slide 38

class Browse(FormView):
    template_name = "shop/index.html"
    form_class = ContactForm
    success_url = reverse_lazy("success")

    # handle the POST request
    def post(self, request):
        response = super().post(request) # use someone else's logic!

        form = ContactForm(request.POST)
        # 1) extract the email, name and reason (use variables to store them)
        if form.is_valid():
            from_email = form.cleaned_data.get("email")
            name = form.cleaned_data.get("name")
            reason = form.cleaned_data.get("reason")

            message = f"{name} from {from_email} said: {reason}"
            subject = "You've got mail."
            recipient_list = ["michel.holzky@gmail.com",]
            send_mail(subject, message, from_email, recipient_list)
            # return response # render() , redirect(), 
            # return "hello?"
        else: 
            render(request, "shop/index.html", {"errors": "sorry, new try.", "form": form})
        return response

    
class Product(TemplateView):
    template_name = "shop/product.html"
    # TODO: add a context variable that has the following
    # { "product_title": "Shoes", "price": 49 }
    # show this in the the shop/product.html
    def get_context_data(self, **kwargs):
        return {
            "product_title": "Shoes",
            "price": 49
        }
