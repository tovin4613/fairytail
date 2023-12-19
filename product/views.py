from django.shortcuts import render
import json
from .models import Post
from django.views import View
from django.http import JsonResponse
from rest_framework import viewsets, status
from .serializer import boardSerializer
from rest_framework.response import Response

# Create your views here.

class boardviewset(viewsets.ModelViewSet):      #<- 추가 (게시판 글 보기)
    queryset=Post.objects.all()
    serializer_class = boardSerializer
    basename='board'
    def get(self, request):
        queryset = Post.objects.all()
        serializer = boardSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer=boardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)