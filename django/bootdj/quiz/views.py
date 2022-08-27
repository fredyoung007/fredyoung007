from cProfile import label
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse

from django.contrib.auth.models import User
import logging

from .models import Quiz, Question, Choice, Submission

logger = logging.getLogger('bootdj')

class QuizListView(ListView):
    template_name = 'quiz/quiz_list.html'
    context_object_name = 'quiz_list'

    def get_queryset(self):
        quizes = Quiz.objects.order_by('-id')[:10]
        return quizes

class QuizDetailView(DetailView):
    model = Quiz
    context_object_name = 'quiz'
    template_name = 'quiz/quiz_detail.html'

def submitView(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    user = request.user
    submission = Submission(quiz=quiz)
    submission.save()
    choices = extract_answers(request)
    submission.choices.add(*choices)
    logger.info(choices)

    return redirect('show_quiz_result', quiz_id=quiz_id, submission_id=submission.id)

def extract_answers(request):
    submitted_anwsers = []
    for key in request.POST:
        if key.startswith('choice'):
            choice_id = int(key.split('_')[1])
            choice_rate = int(request.POST[key])
            choice = Choice.objects.get(pk=choice_id)
            choice.rate = choice_rate
            choice.save()
            submitted_anwsers.append(choice)
    return submitted_anwsers

def show_quiz_result(request, quiz_id, submission_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    submission = Submission(id=submission_id)
    context = {}
    context['quiz'] = quiz
    choicesa = submission.choices.filter(question_id=1)
    choicesb = submission.choices.filter(question_id=2)

    # analytics
    la = [ca.rate for ca in choicesa]
    lb = [cb.rate for cb in choicesb]
    sl = [sum(value) for value in zip(la, lb)]

    roledict = {}
    for i in range(len(sl)):
        roledict[i+1] = sl[i]
    
    sorted_role = sorted(roledict.items(), key=lambda x: x[1], reverse=True)     
    context['sorted_role'] = sorted_role[:2]

    return render(request, 'quiz/quiz_result.html', context)

