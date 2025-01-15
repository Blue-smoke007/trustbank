from django.db import models

# Create your models here.
class CardManagement(models.Model):
    name=models.CharField(max_length=255,null=True,blank=True)
    card_number=models.CharField(max_length=25,null=True,blank=True)
    card_date=models.DateField(auto_now_add=True,null=True,blank=True)
    card_cvv=models.CharField(max_length=5,null=True,blank=True)
