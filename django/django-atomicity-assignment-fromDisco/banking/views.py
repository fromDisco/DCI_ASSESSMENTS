from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist

from .models import Customer, Transaction
from .forms import NewCustomerForm, TransactionForm

# Create your views here.
def index(request):
    """
    Render page with all customers
    """
    customers = Customer.objects.all()
    return render(request, "banking/index.html", {"customers": customers})


def customer_details(request, id):
    """
    Render details page of customer
    """
    customer = Customer.objects.get(id=id)
    # display amount in Euro instead of cents
    customer.amount = format(customer.amount / 100, ".2f")
    return render(request, "banking/customer-details.html", {"customer": customer})


def new_customer(request):
    """
    if request.method == GET
        render form to add new Customer
    if request.method == POST
        save new Customer to DB
    """
    if request.method == "POST":
        form = NewCustomerForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data.get("name")
            # read amount and convert to cents
            amount = form.cleaned_data.get("amount") 
            # Create instance and write to db
            Customer.objects.create(name=name, amount=amount)

        return redirect(reverse("index"))
    else:
        form = NewCustomerForm()
        return render(request, "banking/new-customer.html", {"form": form})


def transfer_money(request, id):
    """
    if request.method == GET
        render form to send money
    if request.method == POST
        send money to reciever,
        substract money from sender
    """

    if request.method == "POST":
        form = TransactionForm(request.POST)

        if form.is_valid():
            sender_name = form.cleaned_data.get("sender")
            reciever_name = form.cleaned_data.get("reciever")
            # read amount and convert to cents
            transfer_amount = form.cleaned_data.get("amount") 

            # block rows while transaction is running
            sender_instance = Customer.objects.select_for_update().get(name=sender_name)
            try:
                # check if user exists
                reciever_instance = Customer.objects.select_for_update().get(
                    name=reciever_name
                )
            except (NameError, ObjectDoesNotExist) as err:
                # prepopulate sender field. Its not editable
                form = TransactionForm(initial={"sender": sender_name})
                data = {
                    "form": form,
                    "message": "No known reciever. Please check your inputs.",
                    "sender": sender_instance,
                    "error": err,
                }
                return render(request, "banking/transaction.html", data)

            if sender_name == reciever_name:
                form = TransactionForm(initial={"sender": sender_name})
                sender_instance.amount = format(sender_instance.amount / 100, ".2f")
                return render(
                    request,
                    "banking/transaction.html",
                    {
                        "form": form,
                        "message": "Not allowed to send money to yourself",
                        "sender": sender_instance,
                    },
                )

            if sender_instance.amount - transfer_amount < sender_instance.overdraft:
                form = TransactionForm(initial={"sender": sender_name})
                # recalculate sender money for view
                sender_instance.amount = format(sender_instance.amount / 100, ".2f")
                overdraft = format(sender_instance.overdraft / 100, ".2f")
                return render(
                    request,
                    "banking/transaction.html",
                    {
                        "form": form,
                        "message": "Not enough money. Amnet the amount.",
                        "overdraft": f"Your maximum overdraft is {overdraft}",
                        "sender": sender_instance,
                    },
                )

            # check if transaction is working, otherwise roll back
            with transaction.atomic():
                # store transaction into db
                money_transfer = Transaction.objects.create(
                    sender=sender_instance,
                    reciever=reciever_instance,
                    amount=transfer_amount,
                )

                sender_instance.amount -= money_transfer.amount
                sender_instance.save()

                reciever_instance.amount += money_transfer.amount
                reciever_instance.save()



            return redirect(
                reverse("customer-details", kwargs={"id": sender_instance.id})
            )
    else:
        sender_instance = get_object_or_404(Customer, id=id)
        # display amount in Euro instead of cents
        sender_instance.amount = format(sender_instance.amount / 100, ".2f")
        # prepopulate sender field. Its not editable
        form = TransactionForm(initial={"sender": sender_instance.name})
        data = {"form": form, "sender": sender_instance}
        return render(request, "banking/transaction.html", data)
