from django.test import TestCase
from django.urls import reverse
from django.http import HttpRequest

from .models import Customer, Transaction
from .forms import TransactionForm, NewCustomerForm


def create_customers(name="", amount=0):
    return Customer.objects.create(name=name, amount=amount)


def set_http_request(user1, user2, amount):
    request = HttpRequest()
    request.POST = {"sender": user1, "reciever": user2, "amount": amount}
    return request


class CustomerIndexViewTest(TestCase):
    def test_list_customers(self):
        create_customers(name="One", amount=50000)
        create_customers(name="Two", amount=0)
        all_customers = Customer.objects.all()

        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

        # set ordered to false, because Querysets are not ordered,
        # but comparison requieres ordering
        self.assertQuerysetEqual(
            response.context["customers"], all_customers, ordered=False
        )

    def test_create_customer_view(self):
        response = self.client.post(
            reverse("new-customer"), {"name": "Three", "amount": 10000.00}
        )
        customer = Customer.objects.all().last()
        self.assertEqual(customer.name, "Three")
        self.assertEqual(customer.amount, 1000000)
        # don't know if it makes sense
        # response is redirected, so 200 isn't the right question
        # self.assertEqual(response.status_code, 302)

    def test_transferForm_is_valid(self):
        user1 = create_customers(name="One", amount=50000)
        user2 = create_customers(name="Two", amount=0)
        amount = 250.00

        request = set_http_request(user1.name, user2.name, amount)
        form = TransactionForm(request.POST)
        # Test if Form is Valid
        self.assertTrue(form.is_valid())

    def test_transferForm_is_not_valid(self):
        user1 = create_customers(name="One", amount=50000)
        user2 = create_customers(name="Two", amount=0)
        # set username to empty string
        user2.name = ""
        amount = 250.00

        request = set_http_request(user1.name, user2.name, amount)
        form = TransactionForm(request.POST)
        # Test if Form is Valid
        self.assertFalse(form.is_valid())

    def test_transfer_money(self):
        user1 = create_customers(name="One", amount=50000)
        user2 = create_customers(name="Two", amount=0)
        amount = 250.00

        response = self.client.post(
            f"/banking/transfer-money/{user1.id}",
            data={"sender": user1.name, "reciever": user2.name, "amount": amount},
        )

        # read new data from Database
        user1_after = Customer.objects.get(id=user1.id)
        user2_after = Customer.objects.get(id=user2.id)

        # check if the old amounts are still in db
        self.assertNotEqual(50000, user1_after.amount)
        self.assertNotEqual(0, user2_after.amount)
        # check if new amounts are correct
        # user1 transfered 25000 from 50000
        # so user1.amount should be 25000
        # user2.amount should also be 25000, before it was 0
        self.assertEqual(25000, user1_after.amount)
        self.assertEqual(25000, user2_after.amount)

    def test_transfer_money_with_wrong_name(self):
        user1 = create_customers(name="One", amount=50000)
        user2 = create_customers(name="Two", amount=0)
        user2.name = "Three"
        amount = 250.00

        request = set_http_request(user1.name, user2.name, amount)
        form = TransactionForm(request.POST)

        response = self.client.post(
            f"/banking/transfer-money/{user1.id}",
            data={"sender": user1.name, "reciever": user2.name, "amount": amount},
        )

        # if customer isn't found error is passed in args
        text = ("Customer matching query does not exist.",)
        self.assertEqual(response.context.get("error").args, text)

        # read data from Database
        user1_after = Customer.objects.get(id=user1.id)
        user2_after = Customer.objects.get(id=user2.id)

        # check if the old amounts are still in db
        self.assertEqual(50000, user1_after.amount)
        self.assertEqual(0, user2_after.amount)
