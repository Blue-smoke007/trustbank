from rest_framework import viewsets
from rest_framework.response import Response
from core_root_api.job_api.serializer.job import JobSerializer
from core_root_api.job_api.models import Job
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser

class JobViewsets(viewsets.ModelViewSet):
    serializer_class=JobSerializer
    queryset=Job.objects.all()
    http_method_names=['get','post','patch','delete']
    parser_classes=[MultiPartParser,FormParser]

    def create(self,request):
        serializer=self.serializer_class(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response({"status":True,"message":"Posted a job successfully"},status=status.HTTP_200_OK)
            else:
                return Response({"status":False,"error_message":"invalid data"},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status":False,"error_message":"Could not post data"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            