from django.shortcuts import render
from django.http import HttpResponse
from api.models import Member, Trip, Action, Comment, Favorite, Following

import django_filters
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Member
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

class MemberFilter(django_filters.FilterSet):
    class Meta:
        model = Member
        fields = {'created_time': ['gte']}

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all().order_by("created_time")

    serializer_class = MemberSerializer
    filter_class = MemberFilter

    # authentication_classes = (SessionAuthentication, BasicAuthentication)
    # permission_classes = (IsAuthenticated,)

# Trip
class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'

class TripFilter(django_filters.FilterSet):
    class Meta:
        model = Trip
        fields = {'created_time': ['gte']}

class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all().order_by("created_time")

    serializer_class = TripSerializer
    filter_class = TripFilter

    # authentication_classes = (SessionAuthentication, BasicAuthentication)
    # permission_classes = (IsAuthenticated,)

# Action
class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = '__all__'

class ActionFilter(django_filters.FilterSet):
    class Meta:
        model = Action
        fields = {'created_time': ['gte']}

class ActionViewSet(viewsets.ModelViewSet):
    queryset = Action.objects.all().order_by("created_time")

    serializer_class = ActionSerializer
    filter_class = ActionFilter

    # authentication_classes = (SessionAuthentication, BasicAuthentication)
    # permission_classes = (IsAuthenticated,)

# Comment
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class CommentFilter(django_filters.FilterSet):
    class Meta:
        model = Comment
        fields = {'created_time': ['gte']}

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by("created_time")

    serializer_class = CommentSerializer
    filter_class = CommentFilter

    # authentication_classes = (SessionAuthentication, BasicAuthentication)
    # permission_classes = (IsAuthenticated,)

# Favorite
class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'

class FavoriteFilter(django_filters.FilterSet):
    class Meta:
        model = Favorite
        fields = {'created_time': ['gte']}

class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all().order_by("created_time")

    serializer_class = FavoriteSerializer
    filter_class = FavoriteFilter

    # authentication_classes = (SessionAuthentication, BasicAuthentication)
    # permission_classes = (IsAuthenticated,)

# Following
class FollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Following
        fields = '__all__'

class FollowingFilter(django_filters.FilterSet):
    class Meta:
        model = Following
        fields = {'created_time': ['gte']}

class FollowingViewSet(viewsets.ModelViewSet):
    queryset = Following.objects.all().order_by("created_time")

    serializer_class = FollowingSerializer
    filter_class = FollowingFilter

    # authentication_classes = (SessionAuthentication, BasicAuthentication)
    # permission_classes = (IsAuthenticated,)

# デフォルトビューの設定
class MainView(TemplateView):
    template_name = 'members/index.html'
