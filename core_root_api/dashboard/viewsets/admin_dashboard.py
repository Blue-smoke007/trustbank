from rest_framework import viewsets
from core_root_api.dashboard.serializers.admin_dashboard import AddCardSerializer,DepositFundSerializer,BlockUserSerializer,UnblockUserSerializer,FreezeUserSerializer,UnfreezeUserSerializer
import random
import datetime
from core_root_api.transactions.models import TransferDetails
from core_root_api.card_management.models import CardManagement
from rest_framework import status 
from rest_framework.response import Response 
from core_root_api.security.user.models import User
import datetime
from core_root_api.dashboard.models import Wallet
from rest_framework.permissions import IsAdminUser
class DepositFundViewset(viewsets.ModelViewSet):
    permission_classes=[IsAdminUser]
    serializer_class=DepositFundSerializer
    http_method_names=['post']
    def create(self,request):
        try:
            serializer=self.serializer_class(data=request.data)
            if serializer.is_valid():
                amount=serializer.validated_data['amount']

                email=serializer.validated_data['email']
                current_user = User.objects.get(email=str(email))
                amount=serializer.validated_data['amount']
                try:
                    user=Wallet.objects.get(user=current_user)
                except Wallet.DoesNotExist:
                    Wallet.objects.update_or_create(user=current_user,balance=0)
                # print("no")
                user=Wallet.objects.get(user=current_user)
                
                balance=user.balance
                print(balance)
                current_balance=balance+float(amount)
                user.balance=current_balance

                user.save()
                TransferDetails.objects.create(user=current_user,amount=amount,description="Deposit",date_created=datetime.date.today(),email=email)
                

                return Response({"status":True,"message":f"Admin Deposited money to user with name {current_user.first_name} {current_user.last_name}"},status=status.HTTP_200_OK)
            else:
                return Response({"status":False,"error":"invalid data"},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status":False,"error":f"Could not deposit money ,internal server error {e}"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AddCardViewset(viewsets.ModelViewSet):
    permission_classes=[IsAdminUser]
    serializer_class=AddCardSerializer
    http_method_names=['get','post']
    def create(self,request):
        try:
            serializer=self.serializer_class(data=request.data)
            if serializer.is_valid():
                email=serializer.validated_data['email']
                card_number=serializer.validated_data['card_number']
                card_cvv = random.randint(100, 999)
                current_user = User.objects.get(email=str(email))

                # Add 5 years to the current date

                # Current date
                card_date = datetime.date.today()

                # Add 5 years to the current date
                try:
                    card_expiry_date = card_date.replace(year=card_date.year + 5)
                except ValueError:
                    # Handle February 29 case for leap years
                    card_expiry_date = card_date + (datetime.date(card_date.year + 5, 3, 1) - datetime.date(card_date.year, 3, 1))

                CardManagement.objects.create(
                    user=current_user,  # Pass the User object directly
                    name=f"{current_user.first_name} {current_user.last_name}",
                    card_date=datetime.date.today(),
                    card_expiry_date=card_expiry_date,
                    card_number=str(card_number),
                    card_cvv=str(card_cvv)
                      # Convert card_cvv to a string
                )
                return Response({"status":True,"message":"Admin added card successfully","data":serializer.validated_data})
            else:
                return Response({"status":False,"error":"Invalid data","data":serializer.validated_data},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status":False,"error":f"Internal server error {e}"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class BlockUserViewset(viewsets.ModelViewSet):
    permission_classes=[IsAdminUser]
    serializer_class=BlockUserSerializer
    http_method_names=['post']
    def create(self,request):
        try:
            serializer=self.serializer_class(data=request.data)
            if serializer.is_valid():
                email=serializer.validated_data['email']
                user=User.objects.get(email=str(email))
                user.is_active=False
                user.save()
                return Response({"status":True,"message":"User blocked and no more active "},status=status.HTTP_200_OK)
            else:
                return Response({"status":False,"error":"invalid data"},status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"status":False,"error":"Try again later, internal server error"})


class UnblockUserViewset(viewsets.ModelViewSet):
    permission_classes=[IsAdminUser]
    serializer_class=BlockUserSerializer
    http_method_names=['post']
    def create(self,request):
        try:
            serializer=self.serializer_class(data=request.data)
            if serializer.is_valid():
                email=serializer.validated_data['email']
                user=User.objects.get(email=str(email))
                user.is_active=True
                user.save()
                return Response({"status":True,"message":"User unblocked and now active "},status=status.HTTP_200_OK)
            else:
                return Response({"status":False,"error":"invalid data"},status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"status":False,"error":"Try again later, internal server error"})

class FreezeUserViewset(viewsets.ModelViewSet):
    permission_classes=[IsAdminUser]
    serializer_class=FreezeUserSerializer
    http_method_names=['post']
    def create(self,request):
        try:
            serializer=self.serializer_class(data=request.data)
            if serializer.is_valid():
                email=serializer.validated_data['email']
                user=User.objects.get(email=str(email))
                user.is_freeze=True
                user.save()
                return Response({"status":True,"message":"User freezed and cant use the site "},status=status.HTTP_200_OK)
            else:
                return Response({"status":False,"error":"invalid data"},status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"status":False,"error":"Try again later, internal server error"})

class UnfreezeUserViewset(viewsets.ModelViewSet):
    permission_classes=[IsAdminUser]
    serializer_class=UnfreezeUserSerializer
    http_method_names=['post']
    def create(self,request):
        try:
            serializer=self.serializer_class(data=request.data)
            if serializer.is_valid():
                email=serializer.validated_data['email']
                user=User.objects.get(email=str(email))
                user.is_freeze=False
                user.save()
                return Response({"status":True,"message":"User unfreezed and can now use the site"},status=status.HTTP_200_OK)
            else:
                return Response({"status":False,"error":"invalid data"},status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"status":False,"error":"Try again later, internal server error"})