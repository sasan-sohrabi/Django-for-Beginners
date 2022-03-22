from django.test import TestCase
from django.urls import reverse

from posts.models import Posts


class PostModelTest(TestCase):

    def setUp(self):
        Posts.objects.create(post='just a test')

    def test_text_content(self):
        post = Posts.objects.get(id=1)
        expected_object_name = f'{post.post}'
        self.assertEqual(expected_object_name, 'just a test')


class HomePageViewTest(TestCase):  # new

    def setUp(self):
        Posts.objects.create(post='this is another test')

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')
