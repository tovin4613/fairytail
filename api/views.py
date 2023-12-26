from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from product.models import *
from .serializer import *
from rest_framework.generics import *
from django.views.generic.list import BaseListView
from django.views.generic.detail import BaseDetailView
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework import status
# 아래부터 'dasomi'가 추가
import requests
from openai import OpenAI
from google.cloud import speech
import io

# 아래는 'dasomi' 가 추가
client = OpenAI(api_key="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")
# Create your views here.


#chatGPT에게 채팅 요청 API
def chatGPT(request):
    
    completion = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "오늘의 날씨는?"}])
    print(completion)
    result = completion.choices[0].message.content
    
    return HttpResponse(result)

# Google STT API를 이용한 음성 파일 변환
def transcribe_audio(request):
    if request.method == 'POST':
        audio_file = request.FILES['audio']
        client = speech.SpeechClient()

        audio_bytes = audio_file.read()
        audio = speech.RecognitionAudio(content=audio_bytes)
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            language_code='ko-KR')

        response = client.recognize(config=config, audio=audio)
        transcripts = [result.alternatives[0].transcript for result in response.results]

        return JsonResponse({'transcripts': transcripts})
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)
    
    """
    1. set GOOGLE_APPLICATION_CREDENTIALS=C:\Users\user\Desktop\speechto-text-409222-178e315d8f2c.json <- 바탕화면에 있는 키 json파일 설정

2. python manage.py shell 실행

3.from google.cloud import speech    <- shell에 입력
import io

# Google Cloud Speech 클라이언트 초기화
client = speech.SpeechClient()

# 음성 파일 불러오기
file_path = 'C:\\Users\\user\\Desktop\\example.wav'
with io.open(file_path, 'rb') as audio_file:
    content = audio_file.read()

audio = speech.RecognitionAudio(content=content)
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    language_code='ko-KR'
)

# STT 요청 및 응답
response = client.recognize(config=config, audio=audio)

# 결과 출력
for result in response.results:
    print('Transcript:', result.alternatives[0].transcript) <- 입력 후 Enter 두번 텍스트로 변환되는거 확인가능.
    
    """
    
# Create your views here.
# class BookViewSet(viewsets.ModelViewSet):
#     queryset = BookList.objects.all()
#     serializer_class = BookSerializer

class BookListView(ListCreateAPIView):
    queryset = BookList.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [BasicAuthentication, SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookListView2(APIView):
    authentication_classes = [BasicAuthentication, SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request):
        booklist = BookList.objects.all()
        serializer = BookSerializer(booklist, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid(): #유효성 검사
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BookListDetailView2(APIView):
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