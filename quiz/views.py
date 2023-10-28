from django.shortcuts import render, redirect
from django.views import View
from .models import Question, Mark
from django.conf import settings
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.
@method_decorator(login_required, name="dispatch")
class Quiz(View):
    def get(self, request):
        questions = Question.objects.filter(verified=True)
        return render(
            request,
            "quiz/quiz.html",
            {"questions": questions}
        )

    def post(self, request):
        mark = Mark(user=request.user, total=Question.objects.filter(verified=True).count())
        for i in range(1, Question.objects.filter(verified=True).count()+1):
            q = Question.objects.filter(pk=request.POST.get(f"q{i}", 0), verified=True).first()
            if request.POST.get(f"q{i}o", "") == q.correct_option:
                mark.got += 1
        mark.save()
        messages.success(request, "Marks updated")
        return redirect("result")

@method_decorator(login_required, name="dispatch")
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
        count, already_exists = 0, 0
        for i in range(1, settings.GLOBAL_SETTINGS["questions"]+1):
            data = request.POST
            q = data.get(f"q{i}", "")
            o1 = data.get(f"q{i}o1", "")
            o2 = data.get(f"q{i}o2", "")
            o3 = data.get(f"q{i}o3", "")
            o4 = data.get(f"q{i}o4", "")
            co = data.get(f"q{i}c", "")
            if Question.objects.filter(question=q).first():
                already_exists += 1
                continue
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
            count += 1
        if already_exists:
            messages.warning(request, f"{already_exists} questions already exists")
        messages.success(request, f"{count} questions added. Wait until admin not verify it.")
        return redirect("quiz")

@method_decorator(login_required, name="dispatch")
class Result(View):
    def get(self, request):
        results = Mark.objects.filter(user=request.user)
        return render(request, "quiz/result.html", {"results": results})

class Leaderboard(View):
    def get(self, request):
        return render(
            request, 
            "quiz/leaderboard.html", 
            {"results": Mark.objects.all().order_by("-got")[:10]}
        )
