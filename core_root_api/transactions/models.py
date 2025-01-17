from django.db import models
from core_root_api.security.user.models import User
# Create your models here.
class TransferDetails(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    bank_name=models.TextField(null=True,blank=True)
    bank_account_number=models.TextField(null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    iban_number=models.TextField(null=True,blank=True)
    routing_number=models.TextField(null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    date_created=models.DateField(auto_now_add=True,null=True,blank=True)
    amount=models.FloatField(null=True,blank=True)
    currency=models.TextField(null=True,blank=True)
    transfer_fee=models.TextField(null=True,blank=True)
    total_amount=models.TextField(null=True,blank=True)
