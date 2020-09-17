from django.utils import timezone

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404

from pybo.forms import QuestionForm
from pybo.models import Question


@login_required(login_url='common:login')
def question_create(request):
    """
    pybo ask question
    """
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False) # do not save "yet" for form's data. Instead it returns forms modle which contains forms model with data
                                               # reason: e.g.) following "create_date" should be set with another data.

            question.author = request.user
            question.create_date = timezone.now()

            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)
    # ---------------------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------------------- #
@login_required(login_url='common:login')
def question_modify(request, question_id):
    """
    pybo Question Update
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, 'You do not have a right to change it') # throw exception (refer to  form_error.html)
        return redirect('pybo:detail', question_id=question.id)

    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.modify_date = timezone.now()
            question.save()
            return redirect('pybo:detail', question_id=question.id)
    else: # NOTE: question_form.html > form : It does not have any action, which means it calls page itself
        form = QuestionForm(instance=question) # to show orignal subject and content
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)

@login_required(login_url='common:login')
def question_delete(request, question_id):
    """
    pybo Question deletion
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, 'You do not have a right to change it')
        return redirect('pybo:detail', question_id=question.id)
    question.delete()
    return redirect('pybo:index')