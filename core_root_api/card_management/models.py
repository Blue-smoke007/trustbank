from django.db import models
from core_root_api.security.user.models import User
# Create your models here.
class CardManagement(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=255,null=True,blank=True)
    card_number=models.CharField(max_length=25,null=True,blank=True)
    card_date=models.DateField(null=True,blank=True)
    card_cvv=models.CharField(max_length=5,null=True,blank=True)
