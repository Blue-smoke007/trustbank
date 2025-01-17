from rest_framework import routers
from core_root_api.card_management.viewsets.add_card import CardManagementViewset
router=routers.SimpleRouter()
router.register(r'card',CardManagementViewset,basename='card')



urlpatterns=[
    *router.urls
]
