from django.urls import path

from .views import BookApiView

urlpatterns = [
    path('book_list/', view=BookApiView.as_view(), name='book_list_api'),
]