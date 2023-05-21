from django.urls import path
from .views import *
urlpatterns = [
    path("" ,  index , name="index"),
    path("task/" , ViewTask , name="task"),
    path("category/" , ViewCategroy , name="viewCategory"),
    path("api/category/" , apiCategory , name="apiCategory"),
    path("api/task/" , apiTask , name="apiTask"),

]
