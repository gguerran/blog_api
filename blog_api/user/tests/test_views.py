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
from blog_api.user.models import User
from blog_api.user.serializers import CreateUserSerializer
from blog_api.user.views import CreateUserView

# API factory for requests of tests
factory = APIRequestFactory()


class PostViewsTest(TestCase):
    
    def test_create(self):
        """ Test creating objects by route """
        self.data = {
            "email": "test@test.com",
            "password": "1234"
        }
        request = factory.post('/signup/', self.data)
        view = CreateUserView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_login(self):
        """ Test creating objects by route """
        self.data = {
            "email": "test@test.com",
            "password": "1234"
        }
        request = factory.post('/login/', self.data)
        view = CreateUserView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)