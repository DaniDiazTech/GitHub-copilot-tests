from django.test import TestCase

from .models import Post, Category, Tag

# Create your tests here.

class TestPost(TestCase):

    def test_str(self):
        my_title = Post(title='This is a basic title for a basic test case')
        self.assertEquals(str(my_title), 'This is a basic title for a basic test case')

class TestCategory(TestCase):

    def test_str(self):
        category = Category(name='Test Category')
        self.assertEquals(str(category), 'Test Category')

class TestTag(TestCase):

    def test_str(self):
        tag = Tag(name='Test Tag')
        self.assertEquals(str(tag), 'Test Tag')

