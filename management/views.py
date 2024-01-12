from django.shortcuts import redirect, render
from django.urls import reverse
from django.conf import settings
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from quiz.models import Mark, Question
from os.path import join

# Create your views here.
@staff_member_required
def manage(request):
    panel_options = {
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

@staff_member_required
def results(request):
    return render(request, "management/results.html", {"results": Mark.objects.all()})

@staff_member_required
def verify_question(request):
    if request.method == "GET":
        qs = Question.objects.filter(verified=False)
        return render(request, "management/verify_question.html", {"questions": qs})

    else:
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

@staff_member_required
def setting(request):
    if request.method == "GET":
        info = {
            "question_limit": settings.GLOBAL_SETTINGS["questions"]
        }
        return render(request, "management/setting.html", {"info": info})

    else:
        qlimit = int(request.POST.get("qlimit", 10))
        if qlimit > 0:
            settings.GLOBAL_SETTINGS["questions"] = qlimit
            messages.success(request, "You preferences saved") 
        else:
            messages.warning(request, "Question limit can't be 0 or less than 0")
        return redirect("setting")
