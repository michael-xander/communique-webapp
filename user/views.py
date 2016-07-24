from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework import permissions

from .serializers import UserSerializer

"""
Views for the REST API
"""

class UserListAPIView(generics.ListAPIView):
    """
    A view used by the REST API to get a list of Users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

class UserDetailAPIView(generics.RetrieveAPIView):
    """
    A view used by the REST API to get details of a single User.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)
