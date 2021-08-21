from django.urls import path, include
from rest_framework.routers import DefaultRouter

from movie.views import MovieViewSet, ActorViewSet, CommentAPIView
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('movies', MovieViewSet)
router.register('actors', ActorViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('comments/', CommentAPIView.as_view(), name='comments'),
    path('comments/<int:pk>', CommentAPIView.as_view(), name='comments'),
    path('auth/', obtain_auth_token),
]
