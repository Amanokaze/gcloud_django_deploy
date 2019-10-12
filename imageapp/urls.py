from django.urls import path
from imageapp.views import *

urlpatterns = [
    path('upload_image/', UploadFileView.as_view()),
] 
