from rest_framework import routers
from core_root_api.security.auth.viewsets.register import RegisterViewSet,AdminRegisterViewSet
from core_root_api.dashboard.viewsets.admin_dashboard import AddCardViewset,DepositFundViewset,BlockUserViewset,UnblockUserViewset,FreezeUserViewset,UnfreezeUserViewset
from core_root_api.dashboard.viewsets.wallet_viewset import WalletViewset
router=routers.SimpleRouter()


router.register(r'admin-board/add-card',AddCardViewset,basename='add_user_card')

router.register(r'admin-board/deposit-fund',DepositFundViewset,basename='deposit_fund')
router.register(r'admin-board/user/block-user',BlockUserViewset,basename='block_user')
router.register(r'admin-board/user/unblock-user',UnblockUserViewset,basename='unblock_user')

router.register(r'admin-board/user/freeze-user',FreezeUserViewset,basename='freeze_user')
router.register(r'admin-board/user/unfreeze-user',UnfreezeUserViewset,basename='unfreeze_user')
router.register(r'user-wallet',WalletViewset,basename='user_wallet')



urlpatterns=[
    *router.urls
]
