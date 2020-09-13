from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from pybo.models import Question
from .forms import QuestionForm, AnswerForm
# ---------------------------------------- [edit] ---------------------------------------- #
from django.http import HttpResponse


def index(request):
    # return HttpResponse("Welcome to pybo")
    """
    pybo list
    """

    # without paging
    #question_list = Question.objects.order_by('-create_date')  # - means opposite
    #context = {'question_list': question_list}

    #with paging
    # input parameter
    page = request.GET.get('page', '1')  # default value is 1

    question_list = Question.objects.order_by('-create_date')

    # paging
    paginator = Paginator(question_list, 10)  # show 10 per page
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}

    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    """
    pybo content detail
    """
    question = get_object_or_404(Question, pk=question_id)  # question = Question.objects.get(id=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
    """
    pybo answer submit
    """
    question = get_object_or_404(Question, pk=question_id)

    # ---------------------------------------- [edit] ---------------------------------------- #
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)
    # ---------------------------------------------------------------------------------------- #

def question_create(request):
    """
    pybo ask question
    """
    # ---------------------------------------- [edit] ---------------------------------------- #
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False) # do not save "yet" for form's data. Instead it returns forms modle which contains forms model with data
                                               # reason: e.g.) following "create_date" should be set with another data.
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)
    # ---------------------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------------------- #
