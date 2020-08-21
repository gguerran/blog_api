# DRF imports
from rest_framework import serializers

# App imports
from blog_api.post.models import Post

class PostSerializer(serializers.ModelSerializer):
    """ Browser serializer """
    class Meta:
        """ Serializer meta class
        Defines the model of the serializer, the ordering of the list of
        browsers and the fields to be listed.
        """
        model = Post
        ordering = ['created_at']
        fields = ['id', 'title', 'description', 'image_url']
        extra_kwargs = {'created_by': {'required': False}}
