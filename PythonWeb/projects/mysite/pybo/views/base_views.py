from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from pybo.models import Question
from django.db.models import Q, Count # OR searching functionality

def index_old(request):
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

def index(request):
    """
    pybo list
    """

    # input parameter
    page = request.GET.get('page', '1')  # page
    kw = request.GET.get('kw', '')  # search word
    so = request.GET.get('so', 'recent')  # ordering

    # get data
    if so == 'recommend':
        question_list = Question.objects.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date') # - means opposite
    elif so == 'popular':
        question_list = Question.objects.annotate(num_answer=Count('answer')).order_by('-num_answer', '-create_date')
    else:  # recent
        question_list = Question.objects.order_by('-create_date')


    # only when kw has a search value
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # title searching  # note: subject__contains=kw means case sensitive
            Q(content__icontains=kw) |  # content searching
            Q(author__username__icontains=kw) |  # question's username searching
            Q(answer__author__username__icontains=kw)  # answer's username searching
        ).distinct()

    # Pagination
    paginator = Paginator(question_list, 10)  # show 10 per page
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj, 'page': page, 'kw': kw, 'so': so}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    """
    pybo content detail
    """
    question = get_object_or_404(Question, pk=question_id)  # question = Question.objects.get(id=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)
