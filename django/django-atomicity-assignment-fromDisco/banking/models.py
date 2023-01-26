from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    amount = models.IntegerField()
    joining_date = models.DateField(auto_now=True)
    overdraft = models.IntegerField(default=0)

    # def __new__(self, *args, **kwargs):
    #     super(Customer, self).__init__(*args, **kwargs)
    #     self.amount = self.amount * 100
    #     print("AAAAAAAAAAAAAAAAAAAAaaaa")


    def save(self, *args, **kwargs):
        """
        If customer is new, 
        change value of amount from Euro to cents
        """
        if self._state.adding is True:
            self.amount = self.amount * 100
        super(Customer, self).save(*args, **kwargs)

    def __str__(self):
        return f"Customer (id={self.id}, name={self.name}, amount={self.amount}, overdraft={self.overdraft}, joining_date={self.joining_date})"


class Transaction(models.Model):
    sender = models.ForeignKey(
        Customer, on_delete=models.PROTECT, related_name="sender"
    )
    reciever = models.ForeignKey(
        Customer, on_delete=models.PROTECT, related_name="reciever"
    )
    amount = models.IntegerField()
    transaction_date = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
        """
        If money is transfered, 
        change value of amount from Euro to cents
        """
        if getattr(self, "amount_changed", True):
            # before amount gets saved, convert it to cents
            self.amount = self.amount * 100
        super(Transaction, self).save(*args, **kwargs)

    def __str__(self):
        return f"Transaction (id={self.id}, sender={self.sender.name}, reciever={self.reciever.name}, amount={self.amount}, transaction_date={self.transaction_date})"
