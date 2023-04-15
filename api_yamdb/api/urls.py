from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import (CategoriesViewSet, CommentViewSet, GenresViewSet,
                    ReviewViewSet, SignupView, TitlesViewSet, TokenView,
                    UsersViewSet)

app_name = 'api'

router_v1 = SimpleRouter()
router_v1.register(r'users', UsersViewSet, basename='users')
router_v1.register(r'categories', CategoriesViewSet)
router_v1.register(r'genres', GenresViewSet)
router_v1.register(r'titles', TitlesViewSet)
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/token/', TokenView.as_view()),
    path('v1/auth/signup/', SignupView.as_view()),
]
