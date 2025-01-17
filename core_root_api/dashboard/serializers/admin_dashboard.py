from rest_framework import serializers

class DepositFundSerializer(serializers.Serializer):
    email=serializers.CharField()
    amount=serializers.FloatField()

class AddCardSerializer(serializers.Serializer):
    email=serializers.CharField()
    card_number=serializers.CharField()

class BlockUserSerializer(serializers.Serializer):
    email=serializers.CharField()

    
    