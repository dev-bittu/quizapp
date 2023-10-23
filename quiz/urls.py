from django.urls import path
from . import views

urlpatterns = [
    path("", views.Quiz.as_view(), name="quiz"),
    path("add_question/", views.AddQuestion.as_view(), name="add_question"),
    path("result/", views.Result.as_view(), name="result"),
    path("leaderboard/", views.Leaderboard.as_view(), name="leaderboard")
]
