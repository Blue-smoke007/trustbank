from rest_framework import routers
from core_root_api.security.auth.viewsets.register import RegisterViewSet,AdminRegisterViewSet
from core_root_api.dashboard.viewsets.admin_dashboard import AddCardViewset,DepositFundViewset,BlockUserViewset
router=routers.SimpleRouter()


router.register(r'admin-board/add-card',AddCardViewset,basename='add_user_card')

router.register(r'admin-board/deposit-fund',DepositFundViewset,basename='deposit_fund')
router.register(r'admin-board/user/block-user',BlockUserViewset,basename='block_user')


urlpatterns=[
    *router.urls
]
