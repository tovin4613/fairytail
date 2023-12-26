from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from product.models import *
from .serializer import *
from rest_framework.generics import *
from django.views.generic.list import BaseListView
from django.views.generic.detail import BaseDetailView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.
# class BookViewSet(viewsets.ModelViewSet):
#     queryset = BookList.objects.all()
#     serializer_class = BookSerializer

class BookListView(ListCreateAPIView):
    queryset = BookList.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [BasicAuthentication, SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookListDetailView(APIView):
    authentication_classes = [BasicAuthentication, SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return BookList.objects.get(pk=pk)
        except BookList.DoesNotExist:
            raise Http404
    
    # 조회
    def get(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = BookSerializer(book)
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
        serializer = BookSerializer(book, data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 삭제
    def delete(self, request, pk, format=None):
        book = self.get_object(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)      

class BookDetailView(ListCreateAPIView):
    queryset = BookDetail.objects.all()
    serializer_class = BookDetailSerializer
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

class QuizListView(ListCreateAPIView):
    queryset = QuizList.objects.all()
    serializer_class = QuizListSerializer
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

class WordListView(ListCreateAPIView):
    queryset = WordList.objects.all()
    serializer_class = WordListSerializer
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

class AiAudioListView(ListCreateAPIView):
    queryset = AiAudioList.objects.all()
    serializer_class = AiAudioListSerializer
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

class CreateUserView(ListCreateAPIView):
    queryset = User.objects.all()
    model = User
    serializer_class = UserSerializer

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