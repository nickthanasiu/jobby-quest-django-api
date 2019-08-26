from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

# models
from .models import Job

# serializers
from .serializers import JobSerializer


class JobView(APIView):

    def get(self, request):
        jobs = Job.objects.all()
        serializer = JobSerializer(jobs, many=True)

        return Response({ "jobs": serializer.data })

    def post(self, request):
        # get job data from request
        job = request.data.get('job')

        # create Job from above data
        serializer = JobSerializer(data=job)
        if serializer.is_valid(raise_exception=True):
            job_saved = serializer.save()

        return Response({ "success": "Job '{}' created successfully".format(job_saved.company + ' - ' + job_saved.job_title) })


