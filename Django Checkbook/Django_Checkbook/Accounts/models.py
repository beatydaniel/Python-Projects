from django.db import models

# Create your models here.

Type_Choices = {
    ('deposit', 'deposit'),
    ('withdrawal', 'withdrawal'),
}


class Account(models.Model):
    First_Name = models.CharField(max_length=60, default='', blank=True, null=False)
    Last_Name = models.CharField(max_length=60, default='', blank=True, null=False)
    Starting_Balance = models.DecimalField(default=0.00,max_digits=100000000000000, decimal_places=2)

    def __str__(self):
        return self .First_Name


class Information(models.Model):
    date_of_transaction = models.DateTimeField(auto_now=False)
    type_of_transaction = models.CharField(max_length=60, choices=Type_Choices)
    amount = models.DecimalField(default=0.00,max_digits=100000000000000, decimal_places=2)
    description = models.CharField(max_length=300, default="", blank=True)
    account = models.CharField(max_length=60, default="", blank=True)

    def __str__(self):
        return self.account
