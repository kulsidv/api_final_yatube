from django.urls import path, include
from rest_framework_nested import routers

from .views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet, basename='api-posts')
router.register(r'groups', GroupViewSet, basename='api-groups')

comments_router = routers.NestedSimpleRouter(
    router,
    r'posts',
    lookup='post_id',
)
comments_router.register('comments', CommentViewSet, basename='post-comments')

urlpatterns = [
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router.urls)),
    path('v1/', include(comments_router.urls)),
    path('v1/follow/', FollowViewSet.as_view()),
]
