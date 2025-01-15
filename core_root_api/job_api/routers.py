from rest_framework import routers

from core_root_api.job_api.viewset.application_form import ApplicationFormViewset,CompanyApplicationFormViewset
from core_root_api.job_api.viewset.job import JobViewsets

router=routers.SimpleRouter()
router.register(r'apply',ApplicationFormViewset,basename='apply')
router.register(r'job-post',JobViewsets,basename='job-post')
router.register(r'company-job-post',CompanyApplicationFormViewset,basename='company-job-post')




urlpatterns=[
    *router.urls
]

