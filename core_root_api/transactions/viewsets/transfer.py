from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from core_root_api.transactions.models import TransferDetails
from core_root_api.transactions.serializers.transfer import TransferSerializer
from core_root_api.dashboard.models import Wallet
from core_root_api.security.user.permissions import IsAccountNotFrozen
from rest_framework.permissions import IsAuthenticated
class TransferViewSet(viewsets.ModelViewSet):
    http_method_names=['get','post']
    queryset=TransferDetails.objects.all()
    serializer_class=TransferSerializer
    permission_classes=[IsAccountNotFrozen]
    def create(self,request):
        serializer=self.serializer_class(data=request.data)
        try:
            if serializer.is_valid():
                # print("ok")
                amount=serializer.validated_data['amount']
                transfer_fee=1.5
                total_amount=float(amount)+transfer_fee
                try:
                    user=Wallet.objects.get(user=request.user)
                except Wallet.DoesNotExist:
                    Wallet.objects.update_or_create(user=request.user,balance=0)
                print("no")
                user=Wallet.objects.get(user=request.user)
                
                balance=user.balance
                print(balance)
                current_balance=balance-total_amount
                user.balance=current_balance
                user.save()
                serializer.save(user=request.user,transfer_fee=transfer_fee,total_amount=total_amount)
                return Response({"status":True,"message":"Transfered money successfully","data":serializer.validated_data})
            else:
                return Response({"status":False,"error":"Invalid data"},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status":False,"error":f"could not initiate a transfer {e}"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
    def list(self, request):
        try:
            # Filter cards for the authenticated user
            transactions = self.queryset.filter(user=request.user)
            serializer = self.serializer_class(transactions, many=True)
            return Response({"status": True,"message":f"Transactions retrieved for {request.user}", "data": serializer.data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": False, "error": f"Could not fetch transactions{e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)