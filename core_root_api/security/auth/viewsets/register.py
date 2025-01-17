import django.contrib
from core_root_api.security import base_url
from django.shortcuts import redirect
from rest_framework import viewsets
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
import random
from core_root_api.security.user.models import CompanyProfile
import string
from django.views import View
from rest_framework.response import Response
# import resend
from core_root_api.security.auth.utils import generate_token
from django.utils.encoding import force_bytes,DjangoUnicodeDecodeError,force_str
from rest_framework.viewsets import ViewSet
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.contrib import messages
from rest_framework_simplejwt.tokens import RefreshToken
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from core_root_api.security.auth.serializer.register import AdminRegisterSerializer,RegisterSerializer

# the future.
from core_root_api.security.user.models import User
from django.utils import timezone
from drf_yasg.utils import swagger_auto_schema
from core_root_api.dashboard.models import Wallet
# from core.wallet.models import UsdModel
from core_root_api.security.auth.serializer.verify_serializer import VerifySerializer
@swagger_auto_schema(
    request_body=AdminRegisterSerializer,
    responses={200: AdminRegisterSerializer}
)

class RegisterViewSet(viewsets.ModelViewSet):
    serializer_class = RegisterSerializer
    
    permission_classes = (AllowAny,)
    http_method_names = ['post']
    
    def generate_random_link(self,length=20):
        # Define the characters allowed in the link
        characters = string.ascii_letters + string.digits

        # Generate a random link by selecting characters randomly
        random_link = ''.join(random.choice(characters) for _ in range(length))

        return random_link
    
    def create(self, request, *args, **kwargs):
       
        serializer = self.serializer_class(data=request.data)
        email=str(serializer.initial_data['email'])
       
        # print(serializer.initial_data['password'])
        password_length=int(len(serializer.initial_data['password']))
        print(password_length)
        print(type(password_length))
        error_list={}
        if not serializer.is_valid():
            print("not valid")
            if User.objects.filter(email=email).exists():
                # return Response({'message':'User with this email already exists','error':True,'field':'email'},status=status.HTTP_403_FORBIDDEN)
                error_list['email_error']='User with this email already exists'
            if password_length<8:
                # print(password_length)
                # print(type(password_length))
                error_list['password_error']='Password should be at least 8 characters'

            
            # if User.objects.filter(username=username).exists():
            #     error_list['username_error']='username exist'
            # if str(serializer.initial_data['confirm_password'])!=str(serializer.initial_data['password']):
                # error_list['password_mismatch_error']='Password mismatch for confirm password'
            if str(serializer.initial_data['password'])!=str(serializer.initial_data['confirm_password']):
                error_list['error_msg']="Password mismatch"
            # error_list['error_msg']='Could not create account'
            error_list['status']=False
            return Response({'error_list':error_list},status=status.HTTP_406_NOT_ACCEPTABLE)
        # if serializer.is_valid():
        else:
            

            print("validated good")
            email=serializer.validated_data['email']

            user=serializer.save()

            refresh = RefreshToken.for_user(user)
          
            res = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            'user_email':str(serializer.validated_data['email'])
            }
            serializer_data = serializer.data.copy()  # Create a copy of the serializer data
            serializer_data.pop('confirm_password', None) 
            return Response({
                "user": serializer_data,
                "refresh": res["refresh"],
                "token": res["access"],
                'user_email':res['user_email'],
                "is_active":True,
                "status":True,
                "success_msg":"Account creation successful, check email to verify your account"
            }, status=status.HTTP_201_CREATED)   
            

class AdminRegisterViewSet(viewsets.ModelViewSet):
    serializer_class = AdminRegisterSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['post']
    def create(self, request, *args, **kwargs):
       
        serializer = self.serializer_class(data=request.data)
        email=str(serializer.initial_data['email'])
        password_length=int(len(serializer.initial_data['password']))
        print(password_length)
        print(type(password_length))
        error_list={}
        if not serializer.is_valid():
            print("not valid")
            if User.objects.filter(email=email).exists():
                error_list['email_error']='User with this email already exists'
            if password_length<8:
                error_list['password_error']='Password should be at least 8 characters'
            if User.objects.filter(username=username).exists():
                error_list['username_error']='username exist'
            if str(serializer.initial_data['password'])!=str(serializer.initial_data['confirm_password']):
                error_list['error_msg']="Password mismatch"
            error_list['status']=False
            return Response({'error_list':error_list},status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            print("validated good")
            email=serializer.validated_data['email']
            user=serializer.save()
            user.is_superuser=True
            user.is_staff=True
            user.save()
    
            refresh = RefreshToken.for_user(user)

            # CompanyProfile.objects.create(user=user,company_phone_number=serializer.validated_data['company_phone_number'],company_name=serializer.validated_data['company_name'],company_url=serializer.validated_data['company_url'],address=serializer.validated_data['company_address'])
            
            res = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            'user_email':str(serializer.validated_data['email'])
            }
            serializer_data = serializer.data.copy()  # Create a copy of the serializer data
            serializer_data.pop('confirm_password', None) 
            Wallet.objects.create(user=request.user,balance=0)

            return Response({
                "user": serializer_data,
                "refresh": res["refresh"],
                "token": res["access"],
                'user_email':res['user_email'],
                "is_active":True,
                "status":True,
                "success_msg":"Account creation successful, check email to verify your account"
            }, status=status.HTTP_201_CREATED)   
            
    # return Response({'error': 'No unassigned keys available.'}, status=status.HTTP_404_NOT_FOUND)
    # else:
    #     return Response({"error":"User with this Api have an existing api key"},status=status.HTTP_403_FORBIDDEN)
class ActivateAccountView(viewsets.ModelViewSet):
    serializer_class = VerifySerializer
    permission_classes=[AllowAny]
    queryset=User.objects.all()
    http_method_names=['get']
    @action(detail=False, url_path='verify/(?P<email>[^/]+)')
    def verify_account(self, request, email=None):
        # Your logic to activate the account using the email parameter
        user = get_object_or_404(User, email=email)
        
        # Update the _active field to True
        user.is_active=True
        
        user.save()
        return HttpResponseRedirect('https://codeblazeacademy-app.vercel.app/signin')
    