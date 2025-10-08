from django.shortcuts import render
from .models import Project
# Create your views here.

def project_list(request):
    projects = Project.objects.all().order_by("-created_at")
    return render(request, "project_list.html", {"projects": projects})


