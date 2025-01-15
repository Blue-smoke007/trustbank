from rest_framework import viewsets, status, response, decorators
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import HttpResponse
from core_root_api import api_url
import requests
from core_root_api.security.user.models import CompanyProfile
import datetime
from core_root_api.job_api.models import ApplicationForm
import uuid
import json
from core_root_api.security.user.models import User
from core_root_api.job_api.models import ApplicationForm
from core_root_api.job_api.models import Job
# jobs = [ 
#         dict(
#             pk=str(uuid.uuid4()),
#             opening=30,
#             title="software Engineer", 
#             details="Experienced in Node.Js, Java, Spring, Bootstrap, Python and Selenium integration and Unit Testing",
#             salary="26K - 30k Monthly",
#             place='Poland',
#             time=datetime.date.fromisoformat("2024-04-24").isoformat(),
#             image_url="jobs/job_1.jpeg",
#             app_date=datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S"),
#             last_date=datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S"),
#             company_name="Microsoft",
#             status="rejected"
#         ),
#         dict(
#             pk=str(uuid.uuid4()),
#             title="mobile App Engineer",
#             details="Experienced in Flutter or React native for uilding a startup app",
#             opening=10,
#             salary="8k - 10K Monthly",
#             place="USA",
#             time=datetime.date.fromisoformat("2024-04-24").isoformat(),
#             image_url="jobs/job_2.jpeg",
#             app_date=datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S"),
#             last_date=datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S"),
#             company_name="Microsoft",
#             status="pending"
#         ),
#         dict(
#             pk=str(uuid.uuid4()),
#             title="mobile App Developer ",
#             details="Binance is looking for senior mobile app developer with at least 10 years of experience building cross platform application with flutter, firebase and react native. The role is also remote based and also  willing to attend yearly meeting at binance head quarters in your country",
#             opening=10,
#             salary="50k - 100K Monthly",
#             place="USA",
#             time=datetime.date.fromisoformat("2024-04-24").isoformat(),
#             image_url="jobs/job_5.jpeg",
#             app_date=datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S"),
#             last_date=datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S"),
#             company_name="Microsoft",
#             status="accepted"
#         ),
#         dict(
#             pk=str(uuid.uuid4()),
#             opening=30,
#             title="software Engineer", 
#             details="Experienced in Node.Js, Java, Spring, Bootstrap, Python and Selenium integration and Unit Testing",
#             salary="26K - 30k Monthly",
#             place='Poland',
#             time=datetime.date.fromisoformat("2024-04-24").isoformat(),
#             image_url="jobs/job_1.jpeg",
#             app_date=datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S"),
#             last_date=datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S"),
#             company_name="Microsoft"
#         ),
#         dict(
#             pk=str(uuid.uuid4()),
#             title="mobile App Engineer",
#             details="Experienced in Flutter or React native for uilding a startup app",
#             opening=10,
#             salary="8k - 10K Monthly",
#             place="USA",
#             time=datetime.date.fromisoformat("2024-04-24").isoformat(),
#             image_url="jobs/job_2.jpeg",
#             app_date=datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S"),
#             last_date=datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S"),
#             company_name="Microsoft"
#         ),
#         dict(
#             pk=str(uuid.uuid4()),
#             title="mobile App Developer ",
#             details="Binance is looking for senior mobile app developer with at least 10 years of experience building cross platform application with flutter, firebase and react native. The role is also remote based and also  willing to attend yearly meeting at binance head quarters in your country",
#             opening=10,
#             salary="50k - 100K Monthly",
#             place="USA",
#             time=datetime.date.fromisoformat("2024-04-24").isoformat(),
#             image_url="jobs/job_5.jpeg",
#             app_date=datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S"),
#             last_date=datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S"),
#             company_name="Microsoft"
#         ),
#     ]
list_of_jobs=Job.objects.all()
jobs=[]
# title=models.CharField(null=True,blank=True,max_length=1000)
#     company_name=models.CharField(null=True,blank=True,max_length=1000)
#     monthly_salary=models.CharField(null=True,blank=True,max_length=100)
#     description=models.TextField(null=True,blank=True)
#     location=models.TextField(null=True,blank=True)
#     no_of_opening=models.IntegerField(null=True,blank=True)
#     application_starting_date = models.DateTimeField(null=True, blank=True)
#     application_ending_date = models.DateTimeField(null=True, blank=True)
for  job in list_of_jobs:

    jobs.append(
        {
            "pk": str(job.pk),
            "title": job.title,
            "company_name": job.company_name,
            "place": job.location,
            "monthly_salary":job.monthly_salary,
            "no_of_opening":job.no_of_opening,
            "application_starting_date":job.application_starting_date,
            "application_ending_date":job.application_ending_date,
            "description":job.description,
            "job_thumbnail":job.job_thumbnail,
            "job_requirements":job.job_requirements
        }
    )

def landing_page(request):
    return render(request, "landing_page.html")

def about_us(request):
    return render(request, "about_us.html")

def contact_us(request):
    return render(request, "contact_us.html")

def student_login(request):
    if request.method=='POST':
   
        login_data={"email":request.POST['email'],"password":request.POST['password']}
        response=requests.post(f"{api_url.base_url}/login/",json=login_data)

        if response.json()['status']==True:
            response_data=response.json()
            request.session['access_token'] = response_data['data']['access']
            request.session['user_id'] = response_data['data']['user']['id']
            return redirect('joblistpost')
        else:
            return redirect('studentsignup')
    return render(request, "auth/student_login.html")

def student_signup(request):
    if request.method=='POST':
    #      "id": "8fd354acae80425db147021537b75a01",
    # "email": "user@example.com",
    # "gender": "Male",
    # "full_name": "Eze Kc",
    # "password": "pbkdf2_sha256$600000$OkFHzcR0NhzqANQBePh4pb$RI4TgTN3LnWbOyA3kUEHpLXbnYveEPc9htIV6zuuCbk=",
    # "phone_number": "0808219999",
    # "student_id": "2019/24355555"
        signup_data={"email":request.POST['email'],"full_name":request.POST['full_name'],"student_id":request.POST['student_id'],"gender":request.POST['gender'],"password":request.POST['password'],"confirm_password":request.POST['confirm_password'],"phone_number":request.POST['phone_number'],}
        response=requests.post(f"{api_url.base_url}/register/",json=signup_data)
        # print(response.status_code)
        # print(signup_data.)
        if response.json()['status']==True:
            return redirect('studentlogin')

        else:
            return redirect('studentsignup')

    return render(request, "auth/student_signup.html")

def admin_login(request):
    if request.method=='POST':
   
        login_data={"email":request.POST['email'],"password":request.POST['password']}
        response=requests.post(f"{api_url.base_url}/login/",json=login_data)

        if response.json()['status']==True:
            response_data=response.json()
            request.session['access_token'] = response_data['data']['access']
            request.session['user_id'] = response_data['data']['user']['id']
            request.session['full_name']=response_data['data']['user']['full_name']
            
            company=CompanyProfile.objects.get(user__public_id=str(response_data['data']['user']['id']))
            request.session['company_name']=company.company_name
            return redirect('companydashboard')
        else:
            return redirect('adminsignup')
    return render(request, "auth/company_login.html")

def admin_signup(request):
    try:
        if request.method=='POST':
    
            signup_data={"email":request.POST['email'],"full_name":request.POST['full_name'],"password":request.POST['password'],'confirm_password':request.POST['confirm_password'],'company_phone_number':request.POST['company_phone_number'],'company_name':request.POST['company_name'],'company_address':request.POST['company_address'],'company_url':request.POST['company_url']}
            response=requests.post(f"{api_url.base_url}/admin-board/register/",json=signup_data)

            if response.json()['status']==True:
                
                return redirect('adminlogin')

            else:
                return redirect('adminsignup')
    except Exception as e:
        return redirect('adminsignup')

    return render(request, 'auth/company_signup.html')

def job_list_post(request):
    global jobs
    length = 10  # Number of items per page
    query = request.GET.get("query")  # Get the search query from the request

    # Filter jobs based on the search query (case insensitive)
    if query:
        filtered_jobs = [job for job in jobs if query.lower() in job['title'].lower()]
    else:
        filtered_jobs = jobs  # If no query, return all jobs

    # Set up pagination
    pages = Paginator(filtered_jobs, length)
    page_number = request.GET.get("page", 1)
    page_obj = pages.get_page(page_number)

    # Context to be passed to the template
    context = {
        'jobs': filtered_jobs[(int(page_number) * length) - length: (int(page_number) * length)], 
        'page_obj': page_obj,
        "leav": "this is it",  # Optional additional context (remove or modify as needed)
    }

    # Add query to context if present
    if query:
        context['query'] = query

    return render(request, "job/job_list.html", context)

def job_single(request, primary_key):
    if not (single := [i for i in jobs if i['pk'] == primary_key]):
        return redirect('index')
    single = single[0]
    return render(request, 'dashboard/student/detailed_saved_job.html', context={'job':single})

def reset_password(request):
    return render(request, "auth/reset_password.html")

def change_password(request):
    return render(request, "auth/change_password.html")

def company_profile(request):
    return render(request, "job/company_profile.html")

def student_profile(request):
    try:
        user_id=request.session.get('user_id')
        response=requests.get(f"{api_url.base_url}/user/{user_id}")
        print(response.json())
    except Exception as e:
        pass
    return render(request, "job/student_profile.html",response.json())

def admin_profile(request):
    return render(request, "job/admin_profile.html")

"""
    START OF THE STUDENT PART
"""

def student_dashboard(request):
    try:
        user_id = request.session.get('user_id')

        user=User.objects.get(public_id=str(user_id).replace("-",""))
        
        name=user.full_name
    except Exception as e:
        
        return redirect('studentlogin') 
    active_jobs=ApplicationForm.objects.all().filter(user__public_id=str(user_id).replace("-",""))

    list_of_jobs=[]
    for job_applied in active_jobs:
        job_data={"full_name":job_applied.full_name,"email":job_applied.email,"phone_number":job_applied.phone_number,"cover_letter":job_applied.cover_letter,}
        list_of_jobs.append(job_data)
    print(list_of_jobs)
    context= {
        "name":name,
        
        "applied_jobs": list_of_jobs,
        "recommended_jobs": json.dumps(list_of_jobs),
        "saved_jobs": json.dumps(list_of_jobs)
    }
    return render(request, "dashboard/student_dashboard.html", context)


def applied_job(request, job_id):
    if not (single := [i for i in jobs if i['pk'] == job_id]):
        return redirect('index')
    single = single[0]
    content = {'job': single, "leav": "this is it"}
    return render(request, "dashboard/student/applied_job.html", content)

def detailed_saved_job(request, job_id):

    global jobs  # Remove this if jobs is fetched within the function

    # Check the HTTP method
    if request.method == 'POST':
        if 'title' in request.POST:
            print(f"POST Title: {request.POST['title']}")
        else:
            print("POST request made but no 'title' found in the request data.")
        return redirect('index')  # Redirect to index or handle POST differently if needed
    
    # Handle GET request
    single = next((job for job in jobs if job.get('pk') == job_id), None)
    
    if not single:
        print(f"No job found with ID: {job_id}")
        return redirect('index')  # Redirect if job not found

    # Log the job details for debugging
    print(f"Job found: {single}")

    # Save job details in the session for use across views
    request.session['job_title'] = single.get('title', 'Unknown Title')
    request.session['job_description'] = single.get('description', 'No Description Available')

    # Make job details available in the view directly (for debugging or further logic)
    job_title = single.get('title', 'Unknown Title')
    job_description = single.get('description', 'No Description Available')

    # Log session data
    print(f"Session data saved - Title: {job_title}, Description: {job_description}")
    return render(request, 'dashboard/student/detailed_saved_job.html', {"job": single})

"""
    Section for job application
"""

def apply_job(request, job_id):
    if request.method == 'POST':
        if 'title' in request.POST:
            job_title=f"{request.POST['title']}"
            request.session['job_title']=job_title
            # print(job_title)
        else:
            print("POST request made but no 'title' found in the request data.")
        # return redirect('index')  
    return render(request, "job/applied_job.html")


def successful_submission(request, job_id):
    
    if request.method == 'POST':
        access_token = request.session.get('access_token')
        # print(access_token)
        job_title=request.session.get('job_title')
        print(job_title)
        # Retrieve form data
        full_name = request.POST['full_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        cover_letter = request.POST['cover_letter']
        
        # Access the uploaded resume file
        resume = request.FILES['resume']
        
        # Prepare application data
        application_data = {
            'full_name': full_name,
            'email': email,
            'phone_number': phone_number,
            'cover_letter': cover_letter,
            'job_title':job_title
            # Note: 'resume' will be handled separately as a file upload
        }
        
        headers = {"Authorization": f"Bearer {access_token}"}
        
        # Send application data along with the resume file
        response = requests.post(
            f"{api_url.base_url}/job/apply/",
            data=application_data,  # Use 'data' for non-file fields
            files={'resume': resume},  # Use 'files' for the resume upload
            headers=headers
        )
        
        print(response.json())
        
        if response.json().get('status') == True:
            # print("good")
            context=response.json()['data']
            print(context)
            return render(request, "job/successful_submission.html",context=context)
        else:
            
            del request.session['access_token']  # Clear the session
            return redirect('student_login')  # Redirect to login

    return render(request, "job/successful_submission.html")

def withdraw_application(request, job_id):
    
    if request.method == 'POST':
        return redirect('studentdashboard')
    elif request.method == "GET":
        if not (single := [i for i in jobs if i['pk'] == job_id]):
            return redirect('index')
        single = single[0]
        content = {'job': single}
        return render(request, "job/withdraw_application.html", content)
    else:
        return redirect('studentdashboard')

"""
    END OF THE STUDENT SECTION
"""

"""
    START OF THE COMPANY ADMIN SECTION
"""
from django.http import FileResponse
from django.conf import settings
import os

def download_cv(request, filename):
    # Construct the full path to the file
    file_path = os.path.join(settings.MEDIA_ROOT, filename)
    if os.path.exists(file_path):
        # Serve the file as a response
        return FileResponse(open(file_path, 'rb'), content_type='application/pdf')
    else:
        # Handle file not found
        return HttpResponse("File not found.", status=404)
def company_dashboard(request):
    try:
        company_name=request.session.get("company_name")
        user=CompanyProfile.objects.get(user__public_id=str(request.session.get('user_id')))
    except Exception as e:
        return redirect('adminlogin')
    list_of_jobs=Job.objects.all().filter(company_name=company_name)
    jobs=[]
    for  job in list_of_jobs:
        jobs.append(
            {
                "pk": str(job.pk),
                "title": job.title,
                "company_name": job.company_name,
                "place": job.location,
                "monthly_salary":job.monthly_salary,
                "no_of_opening":job.no_of_opening,
                "application_starting_date":job.application_starting_date,
                "application_ending_date":job.application_ending_date,
                "description":job.description,
                "job_thumbnail":job.job_thumbnail,
                "job_requirements":job.job_requirements
            }
        )
    total_jobs=Job.objects.filter(company_name=company_name).count()
    # current_jobs=jobs.filte
    total_applicants_count=ApplicationForm.objects.filter(job__company_name=company_name).count()
    
    return render(request, "dashboard/company_dashboard.html", {'jobs':jobs,'total_applicants_count':total_applicants_count,'total_jobs':total_jobs,"full_name":request.session.get("full_name"),"company_name":company_name})

def post_job(request, job_id=None):

    try:
        company_name=request.session.get("company_name")
    except Exception as e:
        return redirect("adminlogin")
    if request.method == 'POST':
    #      title=models.CharField(null=True,blank=True,max_length=1000)
    # company_name=models.CharField(null=True,blank=True,max_length=1000)
    # monthly_salary=models.CharField(null=True,blank=True,max_length=100)
    # description=models.TextField(null=True,blank=True)
    # location=models.TextField(null=True,blank=True)
    # no_of_opening=models.IntegerField(null=True,blank=True)
    # application_starting_date = models.DateField(null=True, blank=True)
    # application_ending_date = models.DateField(null=True, blank=True)
    # active=models.BooleanField(default=True,null=True,blank=True)
    # job_thumbnail=models.FileField(upload_to='photos',null=True,blank=True)

        access_token = request.session.get('access_token')
        # print(access_token)
        
        # Retrieve form data
        title = request.POST['title']
        company_name=company_name
        monthly_salary = request.POST['monthly_salary']
        description = request.POST['description']
        location=request.POST['location']
        no_of_opening=request.POST['no_of_opening']
        
        application_starting_date = request.POST['application_starting_date']
        application_ending_date = request.POST['application_ending_date']
        job_requirements=request.POST['job_requirements']
        
        # Access the uploaded resume file
        job_thumbnail = request.FILES['job_thumbnail']
        
        # Prepare application data
        application_data = {
            'title': title,
            'company_name': company_name,
            'monthly_salary': monthly_salary,
            'description': description,
            'location':location,
            'no_of_opening':no_of_opening,
            'application_starting_date':application_starting_date,
            'application_ending_date':application_ending_date,
            'job_requirements':job_requirements,
            'active':True,
            # Note: 'resume' will be handled separately as a file upload
        }
        print(application_data)
        headers = {"Authorization": f"Bearer {access_token}"}
        
        # Send application data along with the resume file
        response = requests.post(
            f"{api_url.base_url}/job/job-post/",
            data=application_data,  # Use 'data' for non-file fields
            files={'job_thumbnail': job_thumbnail},  # Use 'files' for the resume upload
            headers=headers
        )
        
        print(response.json())
        
        if response.json().get('status') == True:
            return redirect('companydashboard')
            # print("good")
            # context=response.json()['data']
            # print(context)
            # return render(request, "job/successful_submission.html",context=context)
        
    # if job_id:
    #     if not (single := [i for i in jobs if i['pk'] == job_id]):
    #         return redirect('index')
    #     job = single[0]
    #     form_title = "Edit Job Post"
    # else:
    #     job = None
    #     form_title = "Create Job Post"
    
    # if request.method == 'POST':
    #     return redirect('joblistpost')
    # context = {
    #     'form_title': form_title,
    #     'job': job
    # }
    return render(request, 'dashboard/company/job_management.html')

def job_applications(request, job_id=None):
    try:
        company_name=request.session.get("company_name")
    except Exception as e:
        return redirect("adminlogin")
    applicants=ApplicationForm.objects.all().filter(job__company_name=company_name)
 

    return render(request, 'dashboard/company/job_applications.html', {"applicants":applicants})
