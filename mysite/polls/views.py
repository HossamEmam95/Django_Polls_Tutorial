from django.shortcuts import render
from .models import Question, Choice


def home(request):
    questions = Question.objects.all()
    context = {"questions": questions}

    return render(request, 'home.html', context)


def detail(request, pk):
    question = Question.objects.get(id=pk)
    choices = Choice.objects.filter(question=question)

    context = {
        "question": question,
        "choices": choices,
    }

    return render(request, 'details.html', context)