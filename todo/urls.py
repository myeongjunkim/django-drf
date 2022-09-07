from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()

urlpatterns = [
    path('todo/',TodosAPI.as_view()),
    path('todo/<int:pk>/',TodoAPI.as_view()),
    path('done/',DoneTodosAPI.as_view()),
    path('done/<int:pk>/',DoneTodoAPI.as_view()),

]