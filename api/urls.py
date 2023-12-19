from django.urls import path, include
from rest_framework import routers
from .views import BookViewSet

router = routers.DefaultRouter()
router.register('BookList', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
