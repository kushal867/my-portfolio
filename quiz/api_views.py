from rest_framework import generics
from .models import Question, Score
from .serializers import QuestionSerializer, ScoreSerializer

# CRUD for Questions
class QuestionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

# Leaderboard (list + create scores)
class ScoreListCreateAPIView(generics.ListCreateAPIView):
    queryset = Score.objects.all().order_by("-points", "created_at")
    serializer_class = ScoreSerializer

class ScoreDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
