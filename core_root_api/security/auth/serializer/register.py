from rest_framework import serializers

from core_root_api.security.user.serializers.user import UserSerializer
from core_root_api.security.user.models import User
class RegisterSerializer(UserSerializer):
    password = serializers.CharField(max_length=128, min_length=4, required=True)
    confirm_password=serializers.CharField(max_length=128,min_length=4,required=True)
    

    class Meta:
        model = User
        fields = ['id','first_name','last_name','dob','email','phone_number','password','confirm_password']


    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class AdminRegisterSerializer(UserSerializer):
    company_phone_number=serializers.CharField(required=True)
    company_name=serializers.CharField(required=True)
    company_address=serializers.CharField(required=True)
    company_url=serializers.CharField(required=True)
    password = serializers.CharField(max_length=128, min_length=4, required=True)
    confirm_password=serializers.CharField(max_length=128,min_length=4,required=True)
    

    class Meta:
        model = User
        fields = ['id','email', 'full_name','password','confirm_password','company_phone_number','company_name','company_address','company_url']


    def create(self, validated_data):
        return User.objects.create_user(**validated_data)