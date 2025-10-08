from django.urls import path
from . import api_views

urlpatterns = [
    # Questions
    path("questions/", api_views.QuestionListCreateAPIView.as_view(), name="api-questions"),
    path("questions/<int:pk>/", api_views.QuestionDetailAPIView.as_view(), name="api-question-detail"),

    # Scores
    path("scores/", api_views.ScoreListCreateAPIView.as_view(), name="api-scores"),
    path("scores/<int:pk>/", api_views.ScoreDetailAPIView.as_view(), name="api-score-detail"),
]
