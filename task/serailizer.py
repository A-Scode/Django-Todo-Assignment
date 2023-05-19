from rest_framework import serializers
from .models import Task


class CategorySerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField()
    description = serializers.CharField()
    status = serializers.BooleanField()

    class Meta:
        fields = ['id' , 
                  'name' ,
                  'description' ,
                  'status']
        
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        

