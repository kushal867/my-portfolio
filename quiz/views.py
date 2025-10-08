import random
from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
from .models import Question, Score

# Create your views here.

# Quiz Home
def quiz_home(request):
    """Display 5 random quiz questions."""
    questions = list(Question.objects.all())
    random.shuffle(questions)  # shuffle for randomness
    return render(request, "quiz.html", {"questions": questions[:5]})


#Save Score 
def save_score(request):
    """Save user's score after quiz submission."""
    if request.method == "POST":
        username = request.POST.get("username")
        score = request.POST.get("score")

        if not username or not score:
            return HttpResponseBadRequest("Missing username or score.")

        try:
            score = int(score)
        except ValueError:
            return HttpResponseBadRequest("Invalid score format.")

        # Save score
        Score.objects.create(user=username, points=score)
        return redirect("leaderboard")

    return HttpResponseBadRequest("Invalid request method.")


#Leaderboard
def leaderboard(request):
    """Display top 10 scores."""
    scores = Score.objects.all().order_by("-points", "created_at")[:10]
    return render(request, "leaderboard.html", {"scores": scores})



