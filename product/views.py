from django.shortcuts import render
import json
from .models import Post
from django.views import View
from django.http import JsonResponse
from rest_framework import viewsets, status
from .serializer import *
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView,CreateAPIView,RetrieveAPIView
# Create your views here.

class Postview(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class=PostSerializer
    
class postRetrieveview(CreateAPIView, RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class=PostDetailSerializer
    