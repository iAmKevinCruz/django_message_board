from django.http import response
from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from .models import Post

class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text="Just a test")

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_obj_name = f"{post.text}"
        self.assertEqual(expected_obj_name, "Just a test")

    def test_post_list(self):
        response = self.client.get("/posts/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Message #1")
        self.assertContains(response, "Just a test")

    def test_post_detail(self):
        response = self.client.get("/posts/1/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Message #1")
        self.assertContains(response, "Just a test")

    def test_post_list_uses_correct_templates(self):
        response = self.client.get("/posts/")
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'posts_list.html')

    def test_post_detail_uses_correct_templates(self):
        response = self.client.get("/posts/1/")
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'post_detail.html')

    def test_post_list_reverse(self):
        response = self.client.get(reverse('all_posts'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Message #1")
        self.assertTemplateUsed(response, "posts_list.html")

    def test_post_detail_reverse(self):
        response = self.client.get(reverse('post_detail', args=['1']))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Message #1")
        self.assertTemplateUsed(response, "post_detail.html")

class HomePageViewTest(SimpleTestCase):
    def test_view_url_exists_at_proper_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "base.html")
        self.assertTemplateUsed(response, "home.html")
