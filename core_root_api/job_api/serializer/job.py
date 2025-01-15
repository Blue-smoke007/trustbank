from core_root_api.job_api.models import Job
from rest_framework import serializers

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model=Job
        fields="__all__"