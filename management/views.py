from django.core.exceptions import ViewDoesNotExist
from django.shortcuts import redirect, render
from django.utils.deprecation import RenameMethodsBase
from django.views import View
from django.urls import reverse
from quiz.models import Mark

# Create your views here.
class Manage(View):
    def get(self, request):
        panel_options = {
            "Upload Questions": {
                "link": reverse("upload_question"),
                "btntxt": "Upload"
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


class Results(View):
    def get(self, request):
        return render(request, "management/results.html", {"results": Mark.objects.all()})


class UploadQuestion(View):
    def get(self, request):
        return render(request, "management/upload_question.html")

    def post(self, request):
        qFile = request.FILES["qFile"]
        print(qFile)
        return redirect("manage")

