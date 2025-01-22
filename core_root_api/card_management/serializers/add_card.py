from rest_framework import serializers
from core_root_api.card_management.models import CardManagement

class CardManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model=CardManagement
        exclude=['user','card_expiry_date']