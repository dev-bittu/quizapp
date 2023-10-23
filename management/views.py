from django.core.exceptions import ViewDoesNotExist
from django.shortcuts import redirect, render
from django.utils.deprecation import RenameMethodsBase
from django.views import View
from django.urls import reverse
from django.conf import settings
from quiz.models import Mark
from os.path import join

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
        filepath = join(settings.BASE_DIR, "upload")
        if not filepath.name.endswith(".csv"):
            messages.warn(request, "Only CSV file allowed")
        else:
            with open("questions.csv", "w") as f:
                for chunk in qFile.chunks():
                    f.write(chunk)
            messages.success(request, "CSV file uploaded")
        return redirect("manage")

