from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_list, name="blog"),
    path("<slug:slug>/", views.blog_detail, name="blog-detail"),
    path("category/<slug:slug>/", views.category_posts, name="blog-category"),
]
