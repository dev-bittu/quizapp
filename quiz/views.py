from django.shortcuts import render, redirect
from django.views import View
from .models import Question, Mark
from django.conf import settings
from django.contrib import messages

# Create your views here.
class Quiz(View):
    login_required = True

    def get(self, request):
        questions = Question.objects.all()
        return render(
            request,
            "quiz/quiz.html",
            {"questions": questions}
        )

    def post(self, request):
        mark = Mark(user=request.user, total=len(Question.objects.all()))
        for i in range(1, len(Question.objects.all())+1):
            q = Question.objects.filter(pk=request.POST.get(f"q{i}", 0)).first()
            if request.POST.get(f"q{i}o", "") == q.correct_option:
                mark.got += 1
        mark.save()
        messages.success(request, "Marks updated")
        return redirect("result")



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



class Result(View):
    def get(self, request):
        results = Mark.objects.filter(user=request.user)
        return render(request, "quiz/result.html", {"results": results, "user": request.user})
