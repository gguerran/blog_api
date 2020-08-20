# Python imports
from model_mommy import mommy

# Django imports
from django.test import TestCase

# App imports
from blog_api.user.models import User


class UserTest(TestCase):
    """ User model testing module """

    def setUp(self):
        """ Test class settings """
        self.user = User.objects.create(
            email='test@test.com', password="1234"
            )

    def test_create(self):
        """ Post creation test """
        self.assertTrue(User.objects.exists())
    
    def test_str(self):
        """ Test str object return """
        self.assertEqual('test@test.com', str(self.user))

    def test_email_cannot_be_blank(self):
        """ Test name cannot be blank """
        field = User._meta.get_field('email')
        self.assertFalse(field.blank)
    
    def test_email_cannot_be_null(self):
        """ Test name cannot be blank """
        field = User._meta.get_field('email')
        self.assertFalse(field.null)
    
    def test_password_cannot_be_blank(self):
        """ Test name cannot be blank """
        field = User._meta.get_field('password')
        self.assertFalse(field.blank)
    
    def test_password_cannot_be_null(self):
        """ Test name cannot be blank """
        field = User._meta.get_field('password')
        self.assertFalse(field.null)