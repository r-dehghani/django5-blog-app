from django.urls import path

from .views import PostListView, PostDetailView
urlpatterns = [
    path('post_list/', view=PostListView.as_view(), name="post_list"),
    path('<int:pk>/', view=PostDetailView.as_view(), name="post_detail"),
]