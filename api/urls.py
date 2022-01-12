from django.conf.urls import url

from rest_framework import routers
from api.views import MemberViewSet, TripViewSet, ActionViewSet, CommentViewSet, FavoriteViewSet, FollowingViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'members', MemberViewSet)
router.register(r'trips', TripViewSet)
router.register(r'actions', ActionViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'favorites', FavoriteViewSet)
router.register(r'followings', FollowingViewSet)
