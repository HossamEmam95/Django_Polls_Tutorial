from django.shortcuts import render
from .models import Question, Choice


def home(request):
    questions = Question.objects.all()
    context = {"questions": questions}

    return render(request, 'home.html', context)
