# DRF imports
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

# App imports
from blog_api.user.serializers import CreateUserSerializer
from blog_api.user.models import User

class CreateUserView(generics.CreateAPIView):
    """
    API endpoint that allows Users to be viewed, created, edited and deleted.
    """
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny,)