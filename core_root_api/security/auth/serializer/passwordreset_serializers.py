from rest_framework import serializers
from core_app_root.security.user.models import User,PasswordChangeModel,PasswordResetModel
class PasswordUpdateSerializer(serializers.ModelSerializer):
    # old_password=serializers.CharField(max_length=20)
    # final_password=serializers.CharField(max_length=20)
    # repeat_final_password=serializers.CharField(max_length=20)
    email=serializers.CharField(max_length=1000)
    class Meta:
        model=PasswordChangeModel
        fields='__all__'

class ResetPasswordSerializer(serializers.ModelSerializer):
    email=serializers.CharField(max_length=1000)
    # final_password=serializers.CharField(max_length=20)
    # repeat_final_password=serializers.CharField(max_length=20)
    class Meta:
        model=PasswordResetModel
        fields='__all__'