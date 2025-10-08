from django.urls import path
from . import api_views

urlpatterns = [
    path("projects/", api_views.ProjectListCreateAPIView.as_view(), name="api-projects"),
    path("projects/<int:id>/", api_views.ProjectDetailAPIView.as_view(), name="api-project-detail"),
]
