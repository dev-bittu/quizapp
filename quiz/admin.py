from django.contrib import admin
from .models import Question, Mark

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["id", "question", "creator"]
admin.site.register(Question, QuestionAdmin)

class MarkAdmin(admin.ModelAdmin):
    list_display = ["id", "got", "total", "user"]
admin.site.register(Mark, MarkAdmin)
