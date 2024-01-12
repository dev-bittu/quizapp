from django.urls import path
from . import views

urlpatterns = [
    path("", views.quiz, name="quiz"),
    path("add_question/", views.add_question, name="add_question"),
    path("result/", views.result, name="result"),
    path("leaderboard/", views.leaderboard, name="leaderboard")
]
