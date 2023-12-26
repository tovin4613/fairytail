from django.shortcuts import render
import json
from .models import Post
from django.views import View
from django.http import JsonResponse
from rest_framework import viewsets, status
from .serializer import *
from rest_framework.response import Response
from rest_framework.generics import *
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.

class Postview(ListCreateAPIView):
    authentication_classes = [BasicAuthentication, SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()
    serializer_class=PostSerializer
    
class postRetrieveview(APIView):
    authentication_classes = [BasicAuthentication, SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404
    
    # 조회
    def get(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = PostSerializer(book)
        return Response(serializer.data)

    # # 등록
    # def post(self, request, pk, format=None):
    #     book = self.get_object(pk)
    #     serializer = BookSerializer(book, data=request.data) 
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data) 
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 수정
    def put(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = PostSerializer(book, data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 삭제
    def delete(self, request, pk, format=None):
        book = self.get_object(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)      
    
class commentuploadview(APIView):
    authentication_classes = [BasicAuthentication, SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get_object(self, pk):
        try:
            return comment.objects.get(pk=pk)
        except comment.DoesNotExist:
            raise Http404
    
    # 조회
    def get(self, request, pk,id, format=None):
        book = self.get_object(id)
        serializer = commentSerializer(book)
        return Response(serializer.data)

    # 등록
    def post(self, request, pk, id, format=None):
        book = self.get_object(pk)
        serializer = commentSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 수정
    def put(self, request, pk, id, format=None):
        book = self.get_object(id)
        serializer = commentSerializer(book, data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 삭제
    def delete(self, request, id, format=None):
        book = self.get_object(id)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)