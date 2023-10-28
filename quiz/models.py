from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    question = models.TextField(blank=False, unique=True)
    option1 = models.CharField(blank=False, max_length=150)
    option2 = models.CharField(blank=False, max_length=150)
    option3 = models.CharField(blank=False, max_length=150)
    option4 = models.CharField(blank=False, max_length=150)
    correct_option = models.CharField(max_length=1, blank=False)
    creator = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return f"Question({self.question}, {self.creator})"

class Mark(models.Model):
    total = models.IntegerField(blank=False)
    got = models.IntegerField(blank=False, default=0)
    user = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Mark({self.got}/{self.total}, {self.user})"
