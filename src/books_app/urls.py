from django.urls import path
from .views import BookListView


urlpatterns = [
    path("", view=BookListView.as_view(), name='book_list'),
] 