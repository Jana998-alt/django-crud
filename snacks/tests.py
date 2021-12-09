from django.test import TestCase

# Create your tests here.

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Snack


class Tests(TestCase):
    def __init__(self):
        self.snack = None

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="pass"
        )

        self.snack = Snack.objects.create(
            title="Snack_Test", purchaser='jana', description = "this test is working",
        )

    def test_string_representation(self):
        self.assertEqual(str(self.snack), "Snack_Test")

    def test_snack_content(self):
        self.assertEqual(f"{self.snack.title}", "Snack_Test")
        self.assertEqual(f"{self.snack.description}", "this test is working")
        self.assertEqual(f"{self.snack.purchaser}", 'jana')

    def test_snack_list_view(self):
        response = self.client.get(reverse("snack_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Snack_Test")
        self.assertTemplateUsed(response, "snack_list.html")

    def test_snack_detail_view(self):
        response = self.client.get(reverse("snack_detail", args="1"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "description: this test is working")
        self.assertTemplateUsed(response, "snack_detail.html")

    def test_snack_create_view(self):
        response = self.client.post(
            reverse("snack_create"),
            {
                "title": "snack34",
                "purchaser": "drake",
                "description": "ygibuoihiuhiuyvyu",
            }, follow=True
        )

        self.assertRedirects(response, reverse("snack_detail", args="2"))
        self.assertContains(response, "Details about snack34")

    def test_snack_update_view_redirect(self):
        response = self.client.post(
            reverse("snack_update", args="1"),
            {"title": "Updated title","purchaser":"josh","description":"byhuiojo"}
        )

        self.assertRedirects(response, reverse("snack_detail", args="1"))

    def test_snack_delete_view(self):
        response = self.client.get(reverse("snack_delete", args="1"))
        self.assertEqual(response.status_code, 200)