# Python imports
import json
from model_mommy import mommy

# DRF imports
from rest_framework import status
from rest_framework.test import force_authenticate, APIRequestFactory

# Django imports
from django.test import TestCase, Client
from django.urls import reverse

# App imports
from blog_api.post.models import Post
from blog_api.post.serializers import PostSerializer
from blog_api.post.views import PostViewSet
from blog_api.user.models import User

# API factory for requests of tests
factory = APIRequestFactory()


class PostViewsTest(TestCase):
    """ Project view testing module """
    def setUp(self):
        """ Test class settings """
        self.user = User.objects.create(
            email='test@test.com', password='testword'
        )
        self.user.is_active = True
        self.user.save()
        self.post1 = Post.objects.create(
            title='Post 1', description="testetgvsbdfkvnrv",
            image_url = "https://google.com",
            created_by=self.user
        )
        self.post1.save()

        self.post2 = Post.objects.create(
            title='Post 2', description="testetgvsbdfkvnrv",
            image_url = "https://google.com",
            created_by=self.user
        )
        self.post2.save()

        self.post3 = Post.objects.create(
            title='Post 3', description="testetgvsbdfkvnrv",
            image_url = "https://google.com",
            created_by=self.user
        )
        self.post3.save()
    
    def test_create(self):
        """ Test creating objects by route """
        self.data = {
            "title": "test",
            "description": "testesssss",
            "image_url": "https://mdn.mozillademos.org/files/13931/basic-django.png"
        }
        request = factory.post('/post/', self.data)
        force_authenticate(request, user=self.user)
        view = PostViewSet.as_view({'post':'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_all_project(self):
        """ Return test of all objects """
        request = factory.get('/post/')
        force_authenticate(request, user=self.user)
        view = PostViewSet.as_view({'get': 'list'})
        response = view(request)
        posts = Post.objects.filter(created_by=self.user)
        serializer = PostSerializer(posts, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_project(self):
        """ Return test for a specific object """
        request = factory.get('/post/',)
        force_authenticate(request, user=self.user)
        view = PostViewSet.as_view({'get': 'retrieve'})
        response = view(request, pk=self.post1.pk)
        post = Post.objects.get(pk=self.post1.pk)
        serializer = PostSerializer(post)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_post_by_title(self):
        """ Filter test by object name """
        request = factory.get('/post/', {'title': 'project_create'})
        force_authenticate(request, user=self.user)
        view = PostViewSet.as_view({'get': 'list'})
        response = view(request)
        posts = Post.objects.filter(title='project_create')
        serializer = PostSerializer(posts, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_update(self):
        """ Test updating objects by route """
        data = {
            "title": "test",
            "description": "testesssss",
            "image_url": "https://mdn.mozillademos.org/files/13931/basic-django.png"
        }
        request = factory.post('/post/', data)
        force_authenticate(request, user=self.user)
        view = PostViewSet.as_view({'post':'update'})
        response = view(request, pk=self.post2.pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete(self):
        """ Testing for deleting objects by route """
        request = factory.delete('/post/')
        force_authenticate(request, user=self.user)
        view = PostViewSet.as_view({"delete": "destroy"})
        response = view(request, pk=self.post3.pk)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)