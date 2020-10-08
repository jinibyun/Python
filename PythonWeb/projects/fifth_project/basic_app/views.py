from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View, TemplateView

# function  base view
#def index(request):
#   return render (request, 'basic_app/index.html')

# class base view
class CBView(View):
    def get(self, request):
        return HttpResponse("CLASS BASED VIEW")

# template view
class IndexView(TemplateView):
    template_name = 'basic_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'basic injection'
        return context

