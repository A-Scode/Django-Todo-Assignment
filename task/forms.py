from django.forms import ModelForm
from .models import Category ,Task


class CategoryFrom(ModelForm):
    class Meta:
        model = Category
        exclude = ['id']


class TaskFrom(ModelForm):
    class Meta:
        model = Task
        exclude = ['id']