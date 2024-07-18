from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
from rest_framework import status


from books_app.models import Book




class APITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
        title="Django for APIs",
        subtitle="Build web APIs with Python and Django",
        author="William S. Vincent",
        )
    def test_api_listview(self):
        response = self.client.get(reverse("book_list_api"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 1)
        self.assertContains(response, self.book)
    