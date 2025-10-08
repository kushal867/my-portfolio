from rest_framework import generics
from .models import Project
from .serializers import ProjectSerializer

# List + Create
class ProjectListCreateAPIView(generics.ListCreateAPIView):
    queryset = Project.objects.all().order_by("-created_at")
    serializer_class = ProjectSerializer

# Detail view (Retrieve, Update, Delete)
class ProjectDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
