# Python imports
from model_mommy import mommy

# Django imports
from django.test import TestCase

# App imports
from blog_api.post.models import Post
from blog_api.user.models import User


class PostTest(TestCase):
    """ Post model testing module """

    def setUp(self):
        """ Test class settings """
        self.user = mommy.make(User)
        self.post = Post.objects.create(
            title="projeto teste", description="Loren impsum fnjsnld dnasfnwk",
            image_url="/home/gustavo/navedex_api/navedex_api/navedex_api/core/tests",
            created_by=self.user
            )

    def test_create(self):
        """ Post creation test """
        self.assertTrue(Post.objects.exists())
    
    def test_str(self):
        """ Test str object return """
        self.assertEqual('projeto teste', str(self.post))

    def test_title_cannot_be_blank(self):
        """ Test name cannot be blank """
        field = Post._meta.get_field('title')
        self.assertFalse(field.blank)
    
    def test_title_cannot_be_null(self):
        """ Test name cannot be blank """
        field = Post._meta.get_field('title')
        self.assertFalse(field.null)
    
    def test_description_cannot_be_blank(self):
        """ Test name cannot be blank """
        field = Post._meta.get_field('description')
        self.assertFalse(field.blank)
    
    def test_description_cannot_be_null(self):
        """ Test name cannot be blank """
        field = Post._meta.get_field('title')
        self.assertFalse(field.null)
    
    def test_created_by_cannot_be_blank(self):
        """ Test created_by cannot be blank """
        field = Post._meta.get_field('created_by')
        self.assertFalse(field.blank)

    def test_created_by_can_not_be_null(self):
        """ Test created_by cannot be null """
        field = Post._meta.get_field('created_by')
        self.assertFalse(field.null)