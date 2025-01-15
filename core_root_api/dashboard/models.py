from django.db import models
from core_root_api.security.user.models import User
# Create your models here.
class UserDashboard(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    

class Wallet(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    balance=models.FloatField(null=True,blank=True)

class Transactions(models.Model):
    title=models.TextField(null=True,blank=True)
    amount=models.FloatField(null=True,blank=True)
    