from django.urls import path
from . import api_views

urlpatterns = [
    # Categories
    path("categories/", api_views.CategoryListCreateAPIView.as_view(), name="api-categories"),
    path("categories/<int:pk>/", api_views.CategoryDetailAPIView.as_view(), name="api-category-detail"),

    # Posts
    path("posts/", api_views.PostListCreateAPIView.as_view(), name="api-posts"),
    path("posts/<int:pk>/", api_views.PostDetailAPIView.as_view(), name="api-post-detail"),
]
