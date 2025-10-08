from django.urls import path
from . import views

urlpatterns = [
    path("", views.quiz_home, name="quiz"),
    path("save-score/", views.save_score, name="save-score"),
    path("leaderboard/", views.leaderboard, name="leaderboard"),
]
