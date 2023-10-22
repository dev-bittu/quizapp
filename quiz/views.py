from django.shortcuts import render
from django.views import View
from .models import Question
from django.conf import settings

# Create your views here.
class Quiz(View):
    def get(self, request):
        questions = Question.objects.all()
        return render(
                request,
                "quiz/quiz.html",
                {"questions": questions}
                )


class AddQuestion(View):
    def get(self, request):
        return render(
            request, 
            "quiz/add_questions.html",
            {
                "questions": range(1, settings.GLOBAL_SETTINGS["questions"]+1)
            }
        )
    
    def post(self, request):
        pass
