from django.shortcuts import redirect, render
from django.views import View
from django.urls import reverse
from django.conf import settings
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from quiz.models import Mark, Question
from os.path import join

# Create your views here.
@method_decorator(staff_member_required, name="dispatch")
class Manage(View):
    def get(self, request):
        panel_options = {
            "Upload Questions": {
                "link": reverse("upload_question"),
                "btntxt": "Upload"
            },
            "Verify Questions": {
                "link": reverse("verify_question"),
                "btntxt": "Verify"
            },
            "Get Results": {
                "link": reverse("results"),
                "btntxt": "Get"
            }
        }
        return render(
            request,
            "management/manage.html",
            {"panel_options": panel_options}
        )

@method_decorator(staff_member_required, name="dispatch")
class Results(View):
    def get(self, request):
        return render(request, "management/results.html", {"results": Mark.objects.all()})

@method_decorator(staff_member_required, name="dispatch")
class UploadQuestion(View):
    def get(self, request):
        return render(request, "management/upload_question.html")

    def post(self, request):
        qFile = request.FILES["qFile"]
        filepath = join(settings.BASE_DIR, "upload", "questions.csv")
        if not str(qFile).endswith(".csv"):
            messages.warning(request, "Only CSV file allowed")
        else:
            with open(filepath, "wb") as f:
                for chunk in qFile.chunks():
                    f.write(chunk)
            messages.success(request, "CSV file uploaded")
        return redirect("manage")

@method_decorator(staff_member_required, name="dispatch")
class VerifyQuestion(View):
    def get(self, request):
        qs = Question.objects.filter(verified=False)
        return render(request, "management/verify_question.html", {"questions": qs})

    def post(self, request):
        count = 0
        for q, v in request.POST.items():
            if q.startswith("q") and v == "on":
                id = q[1:]
                q = Question.objects.filter(id=id).first()
                if q is not None:
                    q.verified = True
                    q.save()
                    count += 1
                else:
                    messages.warning(request, f"No question exists with id {id}")
        messages.success(request, f"{count} questions added")
        return redirect("manage")

@method_decorator(staff_member_required, name="dispatch")
class Setting(View):
    def get(self, request):
        info = {
            "question_limit": settings.GLOBAL_SETTINGS["questions"]
        }
        return render(request, "management/setting.html", {"info": info})

    def post(self, request):
        qlimit = int(request.POST.get("qlimit", 10))
        if qlimit > 0:
            settings.GLOBAL_SETTINGS["questions"] = qlimit
            messages.success(request, "You preference saved")
        else:
            messages.warning(request, "Question limit can't be 0 or less than 0")
        return redirect("setting")
