from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import Question, Choice
from .forms import QuestionForm, ChoiceForm


def home(request):
    questions = Question.objects.all()

    context = {"questions": questions}

    return render(request, 'home.html', context)


def detail(request, pk):
    question = Question.objects.get(id=pk)
    choices = Choice.objects.filter(question=question)
    print("heeedeeerererere")
    print(choices)
    context = {
        "question": question,
        "choices": choices,
    }

    return render(request, 'details.html', context=context)


def new_question(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        form = QuestionForm()

    return render(request, 'new_question.html', {"form": form})


def new_choice(request, pk):
    if request.method == "POST":
        question = Question.objects.get(id=pk)
        form = ChoiceForm(request.POST)
        if form.is_valid:
            print(form)
            choice = form.save(commit=False)
            choice.question = question
            choice.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        form = ChoiceForm()
    return render(request, 'new_choice.html', {"form": form})
