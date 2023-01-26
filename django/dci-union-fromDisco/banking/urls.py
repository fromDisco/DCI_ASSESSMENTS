from django.urls import path
from . import views

app_name = "banking"
urlpatterns = [
    path("", views.SendMoneyView.as_view(), name="send_money"),
    path("post-transaction/<data>", views.PostTransactionView.as_view(), name="post_transaction")
]
