from rest_framework import serializers
from .models import Job

class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields = [
            'url',
            'company',
            'job_title',
            'user_interest_rating',
            'user_prospect_rating',
            'img_url',
        ]