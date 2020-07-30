from django.test import TestCase
from django.urls import reverse

# Create your tests here.
from .models import Post


class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text='hell am yes')

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'hell am yes')


class HomePostViewTest(TestCase):
    def setUp(self):

        Post.objects.create(text='this is another test')

    def test_view_url_exists_at_proper_location(self):

        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):

        resp = self.client.get(reverse('post'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('post'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'post.html')