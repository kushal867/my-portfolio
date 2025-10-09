
from django.shortcuts import render, get_object_or_404
from .models import Post, Category

# Create your views here

def blog_list(request):
    query = request.GET.get("q")
    if query:
        posts = Post.objects.filter(title__icontains=query) | Post.objects.filter(content__icontains=query)
    else:
        posts = Post.objects.all().order_by("-created_at")
    return render(request, "blog_list.html", {"posts": posts})

def blog_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog_detail.html", {"post": post})

def category_posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category=category).order_by("-created_at")
    return render(request, "blog_list.html", {"posts": posts, "category": category})
