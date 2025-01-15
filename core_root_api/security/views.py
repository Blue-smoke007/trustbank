from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
import request
from django.shortcuts import render
from django.http import JsonResponse
import base64
import numpy as np
from PIL import Image
from io import BytesIO

from rest_framework.response import Response
from .forms import *
# from core_root_api.security import authenticate
# from core_root_api.security.authenticate import FaceIdAuthBackend
from core_root_api.security.forms import AuthenticationForm
from core_root_api.security.utils import prepare_image
from elibraryplatform import settings
from . import base_url
from rest_framework import status
from .forms import UserCreationForm
app_name='security'
def login(request):
    context={"error_messages":""}
    if request.method == 'POST':
            email=request.POST['email']
            password=request.POST['password']
            signin_data={
                "email":email,
                "password":password,
                }
            
            main_url=base_url.main_url+"login/"
            # user = face_id.authenticate(username=email, password=password, face_id=face_image)
            # if user is not None:
            singin_response=request.post(main_url,json=signin_data)

            if singin_response.status_code==200:
                    
                singin_response=singin_response.json()
                print(singin_response)
                return redirect('dashboard_app:dashboard')
                    
            
            else:
                    # username = form.cleaned_data['email']
                # password = form.cleaned_data['password']
                context={"error_messages":"Check if email and password you entered is correct or not"}
        
    print(context)
    context = context
    return render(request, 'auth/login.html', context)


    


# Create your views here.
def signup(request):
    context={"signupErrorMessages":""}
    if request.method=='POST':
        # form = UserCreationForm(request.POST, request.FILES)
        
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        
        if str(password)==str(confirm_password):
            signup_data={
            "email":email,
            "username":username,
            "password":password,
            "confirm_password":confirm_password
            }
            main_url=base_url.main_url+"register/"
            singup_response=request.post(main_url,json=signup_data)

            if singup_response.status_code==201:
                singup_response=singup_response.json()
                print(singup_response)
                # context="Signup Successful"
                # return render(g)
                return redirect('security:login')
                # return redirect('core_root_api:capture_face', user_id=request.user.id)
                
            
            else:
                context = {"signupErrorMessages":["1. Consider checking if your password is upto 8 characters or if username, email already exists in the database , and also check if you entered and confirmed your password "]}
                # full_url=f"{base_url}auth/login"
        else:
        
            context = {"signupErrorMessages":["1. Consider checking if your password is upto 8 characters or if username, email already exists in the database , and also check if you entered and confirmed your password "]}
            # full_url=f"{base_url}auth/login"
    context=context
    print(context)
    return render(request,'auth/signup.html',context)

def face_recognition(request):
    return render(request,'auth/face-recognition.html')

def register(request):
    if  request.method == 'POST':
        form = UserCreationForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password2']
            # user = authenticate(username=username, password=password)
            # login(request, user)
            return redirect('security:login')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'django_two_factor_face_auth/signup.html', context)






def face_login(request):
    if request.method == 'POST':
        try:
            data = request.json()
            image_data = data['image']
            format, imgstr = image_data.split(';base64,')
            image = Image.open(BytesIO(base64.b64decode(imgstr)))
            image = np.array(image)

            face_encodings = face_recognition.face_encodings(image)
            if face_encodings:
                user = request.user
                
                user.face_encoding(face_encodings[0])
                user.save()
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'error': 'No face detected'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

    return render(request, 'auth/face-recognition.html')
