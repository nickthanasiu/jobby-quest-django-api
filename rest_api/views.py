from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

# import models
from .models import Job

# Create your views here.
class JobView(APIView):

    def get(self, request):
        jobs = Job.objects.all()
        return Response({ "jobs": jobs })