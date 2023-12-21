from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from product.models import *
from .serializer import *
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, UpdateAPIView, DestroyAPIView
from django.views.generic.list import BaseListView
from django.views.generic.detail import BaseDetailView
from rest_framework.response import Response
from django.http import JsonResponse

# Create your views here.
# class BookViewSet(viewsets.ModelViewSet):
#     queryset = BookList.objects.all()
#     serializer_class = BookSerializer

class BookListView(ListCreateAPIView):
    queryset = BookList.objects.all()
    serializer_class = BookSerializer

class BookDetailView(ListCreateAPIView):
    queryset = BookDetail.objects.all()
    serializer_class = BookDetailSerializer

class QuizListView(ListCreateAPIView):
    queryset = QuizList.objects.all()
    serializer_class = QuizListSerializer

class WordListView(ListCreateAPIView):
    queryset = WordList.objects.all()
    serializer_class = WordListSerializer

class AiAudioListView(ListCreateAPIView):
    queryset = AiAudioList.objects.all()
    serializer_class = AiAudioListSerializer

# class BookListRetrieveView(RetrieveAPIView):
#     queryset = BookList.objects.select_related('BookList_id').all()
#     serializer_class = BookSerializer

#     def get_object(self):
#         bookList_id = self.kwargs.get('BookList_id')
#         bookDetail = get_object_or_404(BookDetail, pk=bookList_id)
#         return bookDetail.page

# class BookDetailView(BaseListView):
#     model = BookDetail
#     def get_queryset(self):
#         #paramBook = self.request.GET.get('bookdetail')
#         qs = BookDetail.objects.all()
#         return qs
    
#     def render_to_response(self, context, **response_kwargs):
        
#         qs = list(context['object_list'].values())
#         print(qs)

#         jsonData = {
#             'BookDetail_list': qs,
#         }
#         return JsonResponse(data=jsonData, safe=True, status=200)
    

# class BookDetailRetrieveView(RetrieveAPIView):
#     #queryset = BookDetail.objects.all()
#     serializer_class = BookDetailSerializer
#     lookup_field = 'BookList_id'
#     def get_queryset(self):
#         BookList_id = self.kwargs['BookList_id']
#         print(BookList_id)
#         return list(BookDetail.objects.filter(BookList__id=BookList_id))
    

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