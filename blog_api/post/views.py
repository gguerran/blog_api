# DRF imports
from rest_framework import status, viewsets
from rest_framework import permissions
from rest_framework.response import Response

# App imports
from blog_api.post.models import  Post
from blog_api.post.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    """ API endpoint that allows Navers to be viewed, created, edited and
    deleted.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ('__all__')

    def perform_create(self, serializer):
        """ API endpoint function that configures the authenticated user as the
        creator of the object
        """
        serializer.save(created_by=self.request.user)
    
    def get_queryset(self):
        """ API endpoint function that sets up searches for only objects 
        created by the authenticated user
        """
        return Post.objects.filter(created_by=self.request.user)