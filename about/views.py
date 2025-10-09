from django.shortcuts import render
from projects.models import Project

def home(request):
    recent_projects = Project.objects.order_by('-created_at')[:3]
    return render(request, "home.html", {"recent_projects": recent_projects})
