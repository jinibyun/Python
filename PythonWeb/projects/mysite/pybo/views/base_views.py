from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from pybo.models import Question


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
