from rest_framework import viewsets
from core_root_api.card_management.models import CardManagement
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from core_root_api.card_management.serializers.add_card import CardManagementSerializer
class CardManagementViewset(viewsets.ModelViewSet):
    http_method_names=['get','post']
    queryset=CardManagement.objects.all()
    serializer_class=CardManagementSerializer
    permission_classes=[IsAuthenticated]
    def create(self,request):
        serializer=self.serializer_class(data=request.data)
        try:
            if serializer.is_valid():
                
                serializer.save(user=request.user)
                return Response({"status":True,"message":"Added card successfully","data":serializer.validated_data})
            else:
                return Response({"status":False,"error":"Invalid data"},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status":False,"error":f"could not add card"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)