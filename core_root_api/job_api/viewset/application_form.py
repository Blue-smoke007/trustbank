from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from core_root_api.job_api.models import ApplicationForm
from core_root_api.job_api.serializer.application_form import ApplicationFormSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from core_root_api.job_api.models import Job

class ApplicationFormViewset(viewsets.ModelViewSet):
    queryset=ApplicationForm.objects.all()
    serializer_class=ApplicationFormSerializer
    permission_classes=[IsAuthenticated]
    parser_classes=[MultiPartParser,FormParser]

    def create(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
           
            serializer.save(user=request.user)
            print("ok")

            return Response({"status":True,"message":"Recieved your job application, you will hear from us regarding your application soon","data":serializer.data},status=status.HTTP_200_OK)
        # return Response({"status":True,"message":""},status=status.HTTP_200_OK)
    def list(self, request):
        # Fetch only required fields to improve performance
        queryset = self.queryset.filter(user=request.user).select_related('user').values(
        'id',
        'full_name',
        'email',
        'phone_number',
        'cover_letter',
        'resume'
        )

        return Response({
            "status": True,
            "data": list(queryset)
        }, status=status.HTTP_200_OK)


class CompanyApplicationFormViewset(viewsets.ModelViewSet):
    queryset=ApplicationForm.objects.all()
    serializer_class=ApplicationFormSerializer
    permission_classes=[IsAdminUser]
    parser_classes=[MultiPartParser,FormParser]
    http_method_names=['get']
    # def create(self,request):
    #     serializer=self.serializer_class(data=request.data)
    #     if serializer.is_valid():
           
    #         serializer.save(user=request.user)
    #         print("ok")

    #         return Response({"status":True,"message":"Recieved your job application, you will hear from us regarding your application soon","data":serializer.data},status=status.HTTP_200_OK)
        # return Response({"status":True,"message":""},status=status.HTTP_200_OK)
    def list(self, request):
        # Fetch only required fields to improve performance
        queryset = self.queryset.all().select_related('user').values(
        'id',
        'full_name',
        'email',
        'phone_number',
        'cover_letter',
        'resume',
        'application_date',
        'job_status'
        )

        return Response({
            "status": True,
            "data": list(queryset)
        }, status=status.HTTP_200_OK)