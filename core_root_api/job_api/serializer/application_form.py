from core_root_api.job_api.models import ApplicationForm
from rest_framework import serializers

from rest_framework import serializers
from core_root_api.job_api.models import ApplicationForm, Job

class ApplicationFormSerializer(serializers.ModelSerializer):
    job_title = serializers.CharField(write_only=True)
    resume = serializers.FileField(required=True)

    class Meta:
        model = ApplicationForm
        exclude = ['user', 'job']

    def create(self, validated_data):
        # Extract job_title and remove it from validated_data
        job_title = validated_data.pop('job_title', None)
        user = validated_data.pop('user', None)

        # Fetch the Job instance based on job_title
        job = Job.objects.filter(title=job_title).first()
        if not job:
            raise serializers.ValidationError({"job_title": "Invalid job title."})

        # Create the ApplicationForm instance with the job relationship
        application = ApplicationForm.objects.create(
            job=job,
            user=user,
            **validated_data
        )
        return application
