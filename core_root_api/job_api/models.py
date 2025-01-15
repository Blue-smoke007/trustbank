from django.db import models
from django.db import models
import uuid
from core_root_api.security.user.models import User
# Create your models here.
class Job(models.Model):
    title=models.CharField(null=True,blank=True,max_length=1000)
    company_name=models.CharField(null=True,blank=True,max_length=1000)
    monthly_salary=models.CharField(null=True,blank=True,max_length=100)
    description=models.TextField(null=True,blank=True)
    location=models.TextField(null=True,blank=True)
    no_of_opening=models.IntegerField(null=True,blank=True)
    application_starting_date = models.DateField(null=True, blank=True)
    application_ending_date = models.DateField(null=True, blank=True)
    active=models.BooleanField(default=True,null=True,blank=True)
    job_requirements=models.TextField(null=True,blank=True)
    job_thumbnail=models.FileField(upload_to='photos',null=True,blank=True)


    def __str__(self):
        return self.title
    
    # thumbnail=models.ImageField(upload_to='photos')

# Create your models here.
class ApplicationForm(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    full_name=models.TextField(null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    phone_number=models.CharField(max_length=15,null=True,blank=True)
    cover_letter=models.TextField(null=True,blank=True)
    resume=models.FileField(upload_to='photos',null=True,blank=True)
    job=models.ForeignKey(Job,on_delete=models.CASCADE,null=True,blank=True)
    application_date=models.DateField(auto_now_add=True,null=True,blank=True)
    job_status=models.TextField(null=True,blank=True,default="under_review")

    
    def __str__(self):
        return f"{self.user.full_name} applied for {self.job.title} job"
    
# class RecruiterDashboard(models.Model):
