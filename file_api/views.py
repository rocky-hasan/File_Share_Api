from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import FilelistSerializer
from rest_framework import status
# Create your views here.
from rest_framework.parsers import MultiPartParser

def home(request):
    return render(request, 'home.html')

def download(request,uid):
    return render(request, 'download.html', context={'uid':uid})

class FileUploadApi(APIView):

    parser_classes=[MultiPartParser]
    def get(self,request,format=None):
        
        return Response(request.data) 

    def post(self, request, format=None):
        try:
            serializer = FilelistSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)



