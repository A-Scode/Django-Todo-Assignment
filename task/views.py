from django.shortcuts import render
from .models import *
from .serailizer import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
def index(request):

    return render(request , 'index.html')


def ViewCategroy(request):
    category = Category.objects.all()
    

    view_data = {
        "category" : category
    }


    return render(request , 'viewCategory.html' , view_data)


@api_view(['GET'])
def apiCategory(request):
    category = Category.objects.all()
    category_serailize = CategorySerializer(category , many = True)
    return Response(category_serailize.data)

@api_view(['GET'])
def apiTask(request):
    task = Task.objects.all()
    task_serailize = TaskSerializer(task , many=True)

    return Response(task_serailize.data)