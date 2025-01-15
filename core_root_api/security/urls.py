from django.urls import path
from .views import signup,login
from core_root_api.security import views
app_name='security'
urlpatterns = [
    path("auth/signup/",signup,name='signup'),
    path('auth/login/',login,name='login'),
    path('auth/login/facial/',views.face_login,name='facial')
]
