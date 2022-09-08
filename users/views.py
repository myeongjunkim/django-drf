from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth.models import User

from .serializers import *
from .models import *

# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer