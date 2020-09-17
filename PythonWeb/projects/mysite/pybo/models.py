# ref: https://docs.djangoproject.com/en/3.0/ref/models/fields/#field-types
from django.contrib.auth.models import User
from django.db import models


class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    # related_name must be needed because we need to resolve some ambiquity such as User.question_set
    # we can use, then, current_user.author_question.all()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    modify_date = models.DateTimeField(null=True, blank=True) # null allow, blank=true: form.is_valid() does not check this.

    # NOTE: voting vs question is many to many
    # related_name must be needed because we need to resolve some ambiquity such as User.question_set
    # we can use, then, current_user.voter_question.all()
    voter = models.ManyToManyField(User, related_name='voter_question')

    def __str__(self):
        return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()

    # related_name: please see Question part
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    modify_date = models.DateTimeField(null=True, blank=True)

    # related_name: please see Question part
    voter = models.ManyToManyField(User, related_name='voter_answer')

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE) # note: comment can be either question or answer. Therefore, null=True, blank =True
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE) # note: same as above comment