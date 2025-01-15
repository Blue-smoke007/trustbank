from rest_framework import routers
from core_root_api.transactions.viewsets.transfer import TransferViewSet
router=routers.SimpleRouter()
router.register(r'transfer',TransferViewSet,basename='transfer')



urlpatterns=[
    *router.urls
]
