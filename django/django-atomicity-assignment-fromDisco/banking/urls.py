from django.urls import path
from . import views

# This is valid - below

# app_name = "banking"
urlpatterns = [
    path("", views.index, name="index"),
    path("customer-details/<int:id>", views.customer_details, name="customer-details"),
    path("new-customer/", views.new_customer, name="new-customer"),
    path("transfer-money/<int:id>", views.transfer_money, name="transfer-money"),
]
