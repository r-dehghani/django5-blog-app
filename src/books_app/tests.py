from django.test import TestCase
from django.urls import reverse
from django.test import Client

from .models import Book


class BookTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="a title",
            subtitle="a subtitle",
            author="an author",

        )
        
    
    def test_book_content(self):
        self.assertEqual(self.book.title, "a title")
        self.assertEqual(self.book.author, "an author")
        self.assertEqual(self.book.subtitle, "a subtitle")
    
    def test_book_list_view(self):
        # client = Client()
        response = self.client.get(reverse("book_list"))
        print(response)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "subtitle")
        self.assertTemplateUsed(response, "books_app/book_list.html")

