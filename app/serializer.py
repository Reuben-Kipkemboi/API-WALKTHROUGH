from rest_framework import serializers
from .models import * 


class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'
        
        #To retrieve a single image add an id field in your fields ..for my case have included all the fields