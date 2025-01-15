from rest_framework import routers
from core_root_api.security.user.viewsets.user import UserViewset

router=routers.SimpleRouter()
router.register(r'user',UserViewset,basename='user')


urlpatterns=[
    *router.urls
]
