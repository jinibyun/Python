from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from ..models import Question, Answer


@login_required(login_url='common:login')
def vote_question(request, question_id):
    """
    pybo Question voting
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user == question.author:
        messages.error(request, 'You cannot vote the question you made')
    else:
        question.voter.add(request.user) # note: Even if many-to-many, it does not allow duplication
    return redirect('pybo:detail', question_id=question.id)

@login_required(login_url='common:login')
def vote_answer(request, answer_id):
    """
    pybo Answer voting
    """
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user == answer.author:
        messages.error(request, 'You cannot vote the answer you made')
    else:
        answer.voter.add(request.user)
    return redirect('pybo:detail', question_id=answer.question.id)