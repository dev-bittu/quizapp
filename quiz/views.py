from django.shortcuts import render, redirect
from django.views import View
from .models import Question
from django.conf import settings
from django.contrib import messages

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
    login_required = True
    def get(self, request):
        return render(
            request, 
            "quiz/add_questions.html",
            {
                "questions": range(1, settings.GLOBAL_SETTINGS["questions"]+1)
            }
        )
    
    def post(self, request):
        for i in range(1, settings.GLOBAL_SETTINGS["questions"]+1):
            data = request.POST
            q = data.get(f"q{i}", "")
            o1 = data.get(f"q{i}o1", "")
            o2 = data.get(f"q{i}o1", "")
            o3 = data.get(f"q{i}o1", "")
            o4 = data.get(f"q{i}o1", "")
            co = data.get(f"q{i}c", "")
            question = Question(
                question=q,
                option1=o1,
                option2=o2,
                option3=o3,
                option4=o4,
                correct_option=co,
                creator=request.user
            )
            question.save()
        messages.success(request, "Questions added")
        return redirect("quiz")
