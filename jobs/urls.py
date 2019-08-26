from django.urls import path

from .views import JobView

app_name = 'jobs'

urlpatterns = [
    path('jobs/', JobView.as_view()),
]