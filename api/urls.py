from django.urls import path, include
from rest_framework import routers
from .views import *
from product.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from django.contrib.auth.views import LoginView

# router = routers.DefaultRouter()
# router.register('BookList', BookViewSet)
# router.register('BookDetail', BookDetailViewSet, basename='BookDetail')


urlpatterns = [
    #path('', include(router.urls)),
    path('BookList/', BookListView.as_view()),
    path('BookList/<int:pk>/', BookListDetailView.as_view()),
    # path('BookList2/', BookListView2.as_view()),
    # path('BookList2/<int:pk>', BookListDetailView2.as_view()),
    # path('BookList/<int:pk>/', BookListRetrieveView.as_view()),
    path('BookDetail/', BookDetailView.as_view()),
    path('QuizList/', QuizListView.as_view()),
    path('WordList/', WordListView.as_view()),
    path('AiAudioList/', AiAudioListView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('user/<int:pk>/', GetUser.as_view(), name='login'),
    path('signup/', CreateUserView.as_view(), name='signup'),
    # path('BookDetail/', BookDetailView.as_view()),
    # path('BookDetail/<int:BookList_id>/', BookDetailRetrieveView.as_view()),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('posts/', Postview.as_view()),
    path('posts/<int:pk>/', postRetrieveview.as_view())
]
