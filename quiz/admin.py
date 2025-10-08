from django.contrib import admin
from .models import Question, Score


# Register your models here.

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("question_text", "correct_answer")

@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    list_display = ("user", "points", "created_at")

