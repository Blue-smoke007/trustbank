from rest_framework import serializers
class VerifySerializer(serializers.Serializer):
    confirm_url_end_point=serializers.CharField(max_length=1000)
    