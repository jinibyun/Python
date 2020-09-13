from django import forms
from pybo.models import Question, Answer


# django form
# 1. forms.Form
# forms.ModelForm: It is connected with Model. NOTE: It must has "class Meta" where Model should be defined as below
# When using form.as_p, html form input tag will be automatically generated. Refer to {{ form.as_p }} section in question_form.html
# Automatic generation's disadvantage: bootstrap cannot be applied in that html. there please see "widgets" below
# Therefore, manual form creation is preferred

# django form : ref: https://docs.djangoproject.com/en/3.0/topics/forms/
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']
        labels = {
            'subject': 'Subject',
            'content': 'Content'
        }
        # When using form.as_p, because bootstrap cannot be applied. therefore...
        #widgets = {
        #    'subject': forms.TextInput(attrs={'class': 'form-control'}),
        #    'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        #}

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': 'Content',
        }