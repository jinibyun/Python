from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm


def signup(request):
    """
    create an account
    """
    if request.method == "POST":
        form = UserForm(request.POST) #UserForm class exist in forms.py which we have already created
        if form.is_valid():
            form.save() # At this point, use information is saved over database
            username = form.cleaned_data.get('username') # form.cleaned_data.get: input value will be handled separately
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password) # authenticate, login function: They come from django.contrib.auth
            login(request, user)
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})
# ---------------------------------------------------------------------------------------- #