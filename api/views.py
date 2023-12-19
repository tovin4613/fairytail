from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from product.models import *
from .serializer import *
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, UpdateAPIView
from django.views.generic.list import BaseListView
from rest_framework.response import Response
from django.http import JsonResponse

# Create your views here.
# class BookViewSet(viewsets.ModelViewSet):
#     queryset = BookList.objects.all()
#     serializer_class = BookSerializer

class BookListView(ListAPIView):
    queryset = BookList.objects.all()
    serializer_class = BookSerializer

class BookListRetrieveView(RetrieveAPIView):
    queryset = BookList.objects.all()
    serializer_class = BookSerializer

class BookDetailView(BaseListView):
    model = BookList
    def get_queryset(self):
        paramBook = self.request.GET.get('bookdetail')
        qs = BookList.objects.all()
        return qs
    
    def render_to_response(self, context, **response_kwargs):
        #print(context)
        qs = context['object_list']
        #print(qs)
        temp = ['1']

        jsonData = {
            'temp': temp,
        }
        return JsonResponse(data=jsonData, safe=True, status=200)
    
    

class BookDetailRetrieveView(RetrieveAPIView):
    book = BookList.objects.all()
    queryset = BookDetail.objects.all()
    serializer_class = BookDetailSerializer

# class BookDetailViewSet(viewsets.ModelViewSet):
#     def list(self, request):
#         queryset = BookDetail.objects.all()
#         serializer = BookDetailSerializer(queryset, many=True)
#         return Response(serializer.data)
    
#     def retrieve(self, request, pk):
#         queryset = BookDetail.objects.all()
#         book = get_object_or_404(queryset, pk=pk)
#         serializer = BookDetailSerializer(book)
#         return Response(serializer.data)