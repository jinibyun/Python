# ---------------------------------------- [edit] ---------------------------------------- #
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm): # TIP: mouse right click on "UserCreationForm" > Go To > Type Declaration
    email = forms.EmailField(label="email") # extend property

    class Meta:
        model = User
        fields = ("username", "email")
# ---------------------------------------------------------------------------------------- #