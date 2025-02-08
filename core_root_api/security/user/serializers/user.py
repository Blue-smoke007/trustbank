from rest_framework import serializers
from core_root_api.security.user.models import User

class UserSerializer(serializers.ModelSerializer):
    id=serializers.UUIDField(source='public_id',read_only=True,format='hex')
    created=serializers.DateTimeField(read_only=True)
    updated=serializers.DateTimeField(read_only=True)
    profile_image = serializers.SerializerMethodField()

    

    profile_image = serializers.ImageField(allow_null=True, required=False)

    def to_representation(self, instance):
        """Customize the response to include the default image URL if `profile_image` is not uploaded."""
        data = super().to_representation(instance)
        if not instance.profile_image:
            data['profile_image'] = "https://res.cloudinary.com/drlcmhrcg/image/upload/v1739003221/vurzoqjwqft4zofkwdp3.png"
        return data

  


    class Meta:
        model=User
        fields=['id','username','first_name','last_name','dob','email','phone_number','profile_image','is_active','created','updated']
        read_only_field=['is_active']   

class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password=serializers.CharField(required=True)
    new_password=serializers.CharField(required=True)

class ResetPasswordEmailrequesterializer(serializers.ModelSerializer):
    email=serializers.EmailField(min_length=2)

    class Meta:
        model=User
        fields=['email']
# class SetNewPasswordSerializer(serializers.Serializer):
#     password=serializers.CharField(min_length=2,max_length=100)
#     token=serializers.CharField(min_length=1,write_only=True)
#     uidb64=serializers.CharField(min_length=1,write_only=True)
#     class Meta:
#         fields=['password','token','uidb64']
#         def validate(self,attrs):
#             try:
#                 password=atrr
#