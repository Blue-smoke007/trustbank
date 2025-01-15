from rest_framework import routers
from core_root_api.security.auth.viewsets.register import RegisterViewSet,AdminRegisterViewSet
from core_root_api.security.auth.viewsets.login import LoginViewSet
router=routers.SimpleRouter()
router.register(r'register',RegisterViewSet,basename='register')
# router.register(r'admin-board/register',AdminRegisterViewSet,basename='admin_register')

router.register(r'login',LoginViewSet,basename='login')


urlpatterns=[
    *router.urls
]
