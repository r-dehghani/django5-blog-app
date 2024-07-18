from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Posts

class PostsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create(
            username="test",
            password="test",
            email='example@email.com',
            name='testuser',
        )

        cls.post = Posts.objects.create(
            author=cls.user,
            title='test',
            body='body',

        )

    def test_post_model(self):
        self.assertEqual(self.post.author.username, 'test')
        self.assertEqual(self.post.status, "DF")
        self.assertEqual(self.post.title, "test")
        self.assertEqual(self.post.body, "body")