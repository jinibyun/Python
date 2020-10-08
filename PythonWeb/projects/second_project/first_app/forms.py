from django import forms
from django.core import validators #built-in validator
from first_app.models import User


# custom validator (note: it should be outside of class)
def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("Name Needs to start with z")


class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again:')
    textarea = forms.CharField(widget=forms.Textarea())
    # botcatcher = forms.CharField(required = False, widget = forms.HiddenInput, validators=[validators.MaxLengthValidator(0)]) # extra hidden. It will be rendered ad hidden
    
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("GOTCHA BOT!!")
    
    #     return botcatcher
    
    
    # anoter validation: It is automatically called
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("MAKE SURE EMAILS MATCH!")
        
class NewUserForm(forms.ModelForm):
    class Meta: # connect model to form
        model = User  
        fields = '__all__'
        
        