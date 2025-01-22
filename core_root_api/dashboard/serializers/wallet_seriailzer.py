from rest_framework import serializers
from core_root_api.dashboard.models import Wallet
class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model=Wallet
        exclude=['user']