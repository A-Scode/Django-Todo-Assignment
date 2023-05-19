from django.urls import path
from .views import *
urlpatterns = [
    path("" ,  index , name="index"),
    path("category/" , ViewCategroy , name="viewCategory"),
    path("api/category/" , apiCategory , name="apiCategory"),
    path("api/task/" , apiTask , name="apiTask"),

]
