from django.contrib import admin

# Register your models here.

# ref: https://docs.djangoproject.com/en/3.0/ref/contrib/admin/

from .models import Question

# admin.site.register(Question)
# add search functionality
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']


admin.site.register(Question, QuestionAdmin)