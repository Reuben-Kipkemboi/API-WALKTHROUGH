from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  *
from .serializer import StudentsSerializer
from rest_framework import status

# App views
def home(request):
    return render(request, 'index.html')


def next(request):
    return render(request, 'next.html')


class StudentsList(APIView):
    def get(self, request, format=None):
        #querying from the database(students table)
        students = Students.objects.all()
        serializers = StudentsSerializer(students, many=True)
        
        #JSON RESPONSE
        return Response(serializers.data)
    
    def post(self, request, format=None):
        serializers = StudentsSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    



