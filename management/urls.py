from django.urls import path
from . import views

urlpatterns = [
    path("", views.manage, name="manage"),
    path("results/", views.results, name="results"),
    path("verifiy_questions/", views.verify_question, name="verify_question"),
    path("setting/", views.setting, name="setting")
]
