from rest_framework import serializers
from core_root_api.transactions.models import TransferDetails
class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model=TransferDetails
        exclude=['transfer_fee','total_amount','user']