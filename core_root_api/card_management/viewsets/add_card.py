from rest_framework import viewsets
from core_root_api.card_management.models import CardManagement
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import datetime
from rest_framework import status
from core_root_api.card_management.serializers.add_card import CardManagementSerializer
class CardManagementViewset(viewsets.ModelViewSet):
    http_method_names=['get','post']
    queryset=CardManagement.objects.all()
    serializer_class=CardManagementSerializer
    permission_classes=[IsAuthenticated]

    def list(self, request):
        try:
            # Filter cards for the authenticated user
            user_cards = self.queryset.filter(user=request.user)
            serializer = self.serializer_class(user_cards, many=True)
            return Response({"status": True,"message":"cards retrieved", "data": serializer.data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": False, "error": "Could not fetch cards"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self,request):
        serializer=self.serializer_class(data=request.data)
        try:
            if serializer.is_valid():
                card_date = datetime.date.today()

                # Add 5 years to the current date
                try:
                    card_expiry_date = card_date.replace(year=card_date.year + 5)
                except ValueError:
                    # Handle February 29 case for leap years
                    card_expiry_date = card_date + (datetime.date(card_date.year + 5, 3, 1) - datetime.date(card_date.year, 3, 1))
                serializer.save(user=request.user,card_expiry_date=card_expiry_date)
                return Response({"status":True,"message":"Added card successfully","data":serializer.validated_data})
            else:
                return Response({"status":False,"error":"Invalid data"},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status":False,"error":f"could not add card"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)