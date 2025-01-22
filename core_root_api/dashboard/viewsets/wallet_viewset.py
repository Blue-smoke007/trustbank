from rest_framework import viewsets
from core_root_api.dashboard.serializers.admin_dashboard import AddCardSerializer,DepositFundSerializer,BlockUserSerializer
from core_root_api.dashboard.serializers.wallet_seriailzer import WalletSerializer
import random
from core_root_api.card_management.models import CardManagement
from rest_framework import status 
from rest_framework.response import Response 
from core_root_api.security.user.models import User
import datetime
from core_root_api.dashboard.models import Wallet
from rest_framework.permissions import IsAuthenticated
class WalletViewset(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticated]
    serializer_class=WalletSerializer
    http_method_names=['get']
    def list(self,request):
        try:
            serializer=self.serializer_class(data=request.data)
            if serializer.is_valid():
               
                current_user = User.objects.get(email=request.user.email)
                # print(current_user.first_name)
               
                username=f"{current_user.first_name} {current_user.last_name}"
                try:
                    user=Wallet.objects.get(user=current_user)
                except Wallet.DoesNotExist:
                    Wallet.objects.update_or_create(user=current_user,balance=0)
                # print("no")
                user=Wallet.objects.get(user=current_user)
                
                balance=user.balance
               
                return Response({"status":True,"message":f"Fetched user data successfully","data":{"amount":balance,"username":username}},status=status.HTTP_200_OK)
            else:
                return Response({"status":False,"error":"invalid data"},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status":False,"error":f"Internal server error,try again later "},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
