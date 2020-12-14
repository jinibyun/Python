from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

# function  base view
#def index(request):
#   return render (request, 'basic_app/index.html')

# class base view
from basic_app import models


class CBView(View):
    def get(self, request):
        return HttpResponse("CLASS BASED VIEW") # not even define template

# class based template view
class IndexView(TemplateView):
    template_name = 'basic_app/index.html'

    # NOTE: without below, templateview works, but no data is being passed
    # that is why we will have to defind method as below

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'basic injection'
        return context

class SchoolListView(ListView):
    # NOTE: if you want to change, otherwise use below default settings
    # NOTE: default template view name set to school_list.html

    context_object_name = 'schools'
    model = models.School # NOTE: it returns school_list (lowercaes of model_list)

class SchoolDetailView(DetailView):
    context_object_name = 'school_details' # NOTE: if you want to change, otherwise use below default settings

    # NOTE: default template view name set to school_detail.html
    model = models.School # NOTE: it returns school (lowercaes of model)
    template_name = 'basic_app/school_detail.html'

class SchoolCreateView(CreateView):
    # note: school_form.html is expected
    fields = ('name', 'principal', 'location') # it must be complied with model
    model = models.School

class SchoolUpdateView(UpdateView):
    # note: school_form.html is expected
    fields = ('name', 'principal') # it must be complied with model
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("basic_app:list") #actually delete and redirect