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
 
    class Meta:
        model = User
        fields = ['id','first_name','last_name','dob','email','phone_number','password','confirm_password']


    def create(self, validated_data):
        return User.objects.create_user(**validated_data)