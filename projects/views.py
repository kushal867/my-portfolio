from django.shortcuts import render
from .models import Project
# Create your views here.

def project_list(request):
    projects = Project.objects.all().order_by("-created_at")
    # Build unique technology chips (display label + lowercase key)
    tech_keys = set()
    techs = []
    for p in projects:
        tech_field = (p.technologies or "")
        for raw in tech_field.split(","):
            label = raw.strip()
            if not label:
                continue
            key = label.lower()
            if key not in tech_keys:
                tech_keys.add(key)
                techs.append({"label": label, "key": key})
    return render(request, "project_list.html", {"projects": projects, "techs": techs})


