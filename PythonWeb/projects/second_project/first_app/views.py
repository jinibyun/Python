from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord

from . import forms # . means from current 
from first_app.forms import NewUserForm
# Create your views here.

def index(request):
    # return HttpResponse("Hello World")
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {"access_records":webpages_list}
    return render(request,'first_app/index.html',date_dict)

# Form without Model
def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = forms.FormName(request.POST)
        
        if form.is_valid():
            # just for testing
            print("validation success")
            print("NAME: " + form.cleaned_data['name'])
            print("NAME: " + form.cleaned_data['email'])
            print("NAME: " + form.cleaned_data['textarea'])
    
    return render(request, 'first_app/form.page.html', {'form':form})

# Form with Model Connected (ModelForm)
def users(request):
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True) # actual db save
            return index(request)
        else:
            print("Error from invalid")
            
    return render(request,'first_app/users.html', {'form': form})
            
    
