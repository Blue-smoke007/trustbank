from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings
from django.contrib.auth.models import update_last_login

from core_root_api.security.user.serializers.user import UserSerializer
from core_root_api.security.user.models import User

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings
from django.contrib.auth.models import update_last_login
from core_root_api.security.user.models import User
from rest_framework import serializers
from datetime import timedelta
# class StoreCurrentTokenSerializer(serializers.Serializer):
#     current_token=serializers.CharField()
#     class Meta:
#         model=User
#         fields=['current_token']

class LoginSerializerClass(TokenObtainPairSerializer):
    # ...

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)
        access = refresh.access_token

        # access.set_exp(lifetime=timedelta(hours=100))  # Set access token expiry to 3 hours

        data['user'] = UserSerializer(self.user).data
        data['refresh'] = str(refresh)
        data['access'] = str(access)

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data
    
        
