from django.test import TestCase
from django.urls import reverse

from .models import Comment


class TemplateTests(TestCase):
    def test_homepage_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_articles_page_status_code(self):
        test_uuid = "f52c15f2-c5a9-11e7-8889-0050569d4be0"
        response = self.client.get(f"/article/{test_uuid}")
        self.assertEqual(response.status_code, 200)

    def test_homepage_uses_correct_template(self):
        response = self.client.get(reverse("homepage"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")

    def test_article_uses_correct_template(self):
        test_uuid = "f52c15f2-c5a9-11e7-8889-0050569d4be0"
        response = self.client.get(reverse("article_page", kwargs={"article_uuid": test_uuid}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "article.html")


class CommentModelTests(TestCase):
    def setUp(self):
        self.new_comment = Comment(
            comment="This is my test comment", article_uuid="f52c15f2-c5a9-11e7-8889-0050569d4be0"
        )

    def test_comment_content(self):
        self.assertEqual(f"{self.new_comment.comment}", "This is my test comment")
        self.assertEqual(f"{self.new_comment.article_uuid}", "f52c15f2-c5a9-11e7-8889-0050569d4be0")
