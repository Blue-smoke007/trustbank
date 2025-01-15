from django.db import models

# Create your models here.
class TransferDetails(models.Model):
    bank_name=models.TextField(null=True,blank=True)
    bank_account_number=models.EmailField(null=True,blank=True)
    email=models.TextField(null=True,blank=True)
    iban_number=models.TextField(null=True,blank=True)
    routing_number=models.TextField(null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    amount=models.FloatField(null=True,blank=True)
    currency=models.TextField(null=True,blank=True)
    transfer_fee=models.TextField(null=True,blank=True)
    total_amount=models.TextField(null=True,blank=True)
    