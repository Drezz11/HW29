from django.db.models import Count
from django.shortcuts import render

import json

from django.http import JsonResponse

from django.utils.decorators import method_decorator

from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, CreateView, UpdateView, ListView, DeleteView
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.viewsets import ModelViewSet

from users.models import User, Location

from users.serilizers import *


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


class UserListView(ListAPIView):
    queryset = User.objects.annotate(total_ads=Count("ads", filter=Q(ads__is_published=True))).order_by("username")
    serializer_class = UserListSerializer


class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


class UserUpdateView(UpdateView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializers


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializers


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationModelSerializer
