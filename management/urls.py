from django.urls import path
from . import views

urlpatterns = [
    path("", views.Manage.as_view(), name="manage"),
    path("results/", views.Results.as_view(), name="results"),
    path("upload_questions", views.UploadQuestion.as_view(), name="upload_question"),
    path("verifiy_questions/", views.VerifyQuestion.as_view(), name="verify_question"),
    path("setting/", views.Setting.as_view(), name="setting")
]
