from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                    ReviewViewSet, TitlesViewSet, UserViewSet, get_jwt_token,
                    register)

router_v1 = DefaultRouter()
router_v1.register('users', UserViewSet, basename='Users')
router_v1.register('categories', CategoryViewSet, basename='Category')
router_v1.register('genres', GenreViewSet, basename='Genre')
router_v1.register('titles', TitlesViewSet, basename='Title')
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews', ReviewViewSet, basename='reviews'
)
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comments'
)

auth_patterns = [
    path('signup/', register, name='register'),
    path('token/', get_jwt_token, name='token')
]

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/', include(auth_patterns)),
]
