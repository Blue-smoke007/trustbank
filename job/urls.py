#!/usr/bin/env python3fr
from rest_framework.routers import DefaultRouter
from django.urls import path, include
import job.views as job

# router = DefaultRouter()
# router.register("jobs", job.JobsViewSet, basename="jobviewset")

urlpatterns = [
    # path("student/", include(router.urls)),
    path("", job.landing_page, name="index"),
    path("about-us", job.about_us, name="aboutus"),
    path('contact-us', job.contact_us, name="contactus"),
    path("admin-login", job.admin_login, name="adminlogin"),
    path('job-list', job.job_list_post, name="joblistpost"),
    path("admin-signup", job.admin_signup, name="adminsignup"),
    path("admin-profile", job.admin_profile, name="adminprofile"),
    path('student-login', job.student_login, name="studentlogin"),
    path("apply-job/<str:job_id>", job.apply_job, name="apply-job"),
    path('student-signup', job.student_signup, name="studentsignup"),
    path("reset-password", job.reset_password, name="resetpassword"),
    path("change-password", job.change_password, name="changepassword"),
    path("student-profile", job.student_profile, name="studentprofile"),
    path("company-profile", job.company_profile, name="companyprofile"),
    path("job/applied/<str:job_id>", job.applied_job, name="appliedjob"), 
    path("single-job/<str:primary_key>", job.job_single, name="singlejob"),
    path("student-dashboard", job.student_dashboard, name="studentdashboard"),
    path("student/job/saved/<str:job_id>", job.detailed_saved_job, name="detailedsavedjob"),
    path("successful-submission/<str:job_id>", job.successful_submission, name="submit-application"),
    path("withdraw-application/<str:job_id>", job.withdraw_application, name="withdrawapplication"),
    
    # COMPANY PART
    path("company-dashboard", job.company_dashboard, name="companydashboard"),
    path('job/create/', job.post_job, name='postjob'),
    path('job/edit/<int:job_id>/', job.post_job, name='edit-job'),
    path("job/applications/", job.job_applications, name="jobapplications"),
    path('download-cv/<str:filename>/', job.download_cv, name='download_cv'),
]

