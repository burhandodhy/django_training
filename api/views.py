from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from api.serializers import UserSerializer
from rest_framework import permissions
from api.permissions import IsOwnerOrReadOnly
from authenticate.models import CustomUser



class UserViewSet(viewsets.ModelViewSet):

  serializer_class = UserSerializer
  queryset = CustomUser.objects.all()
  permission_classes = (IsOwnerOrReadOnly,)
  http_method_names = ['get', 'patch', 'post', 'delete']
