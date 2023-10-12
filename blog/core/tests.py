from django.test import TestCase
from .models import Post


class TestModel(TestCase):
    def setUp(self):
        self.blog = Post.objects.create(title='test-post', author='Bekele',
                                        slug='djan')

    def test_post(self):
        d = self.blog
        self.assertTrue(isinstance(d, Post))
        self.assertEqual(str(d), 'test-post')
