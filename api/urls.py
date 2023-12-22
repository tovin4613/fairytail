from django.urls import path, include
from rest_framework import routers
from .views import *
from product.views import *
# router = routers.DefaultRouter()
# router.register('BookList', BookViewSet)
# router.register('BookDetail', BookDetailViewSet, basename='BookDetail')


urlpatterns = [
    #path('', include(router.urls)),
    path('BookList/', BookListView.as_view()),
    # path('BookList/<int:pk>/', BookListRetrieveView.as_view()),
    path('BookDetail/', BookDetailView.as_view()),
    path('QuizList/', QuizListView.as_view()),
    path('WordList/', WordListView.as_view()),
    path('AiAudioList/', AiAudioListView.as_view()),
    # path('BookDetail/', BookDetailView.as_view()),
    # path('BookDetail/<int:BookList_id>/', BookDetailRetrieveView.as_view()),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('posts/', Postview.as_view()),
    path('posts/<int:pk>/', postRetrieveview.as_view())
]
