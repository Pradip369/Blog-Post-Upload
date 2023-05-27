from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,\
    UsernameField
from django.contrib.auth.models import User
from django import forms
from django.utils.translation import gettext ,gettext_lazy as _
from blog.models import Post
from django.contrib.admin import widgets


class SignupForm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs = {'class':'form-control'}))
    password2 = forms.CharField(label='Comform Password',widget=forms.PasswordInput(attrs = {'class':'form-control'}))

    class Meta:
        model = User
        fields = ["username","first_name","last_name","email"]
        labels = {'email':"Email"}
        widgets = {'username':forms.TextInput(attrs = {'class':'form-control'}),
                   'first_name':forms.TextInput(attrs = {'class':'form-control'}),
                   'last_name':forms.TextInput(attrs = {'class':'form-control'}),
                   'email':forms.EmailInput(attrs = {'class':'form-control'}),
                   }
        
        
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs = {'autofocus':True,'class':'form-control'}))
    password = forms.CharField(label = _("password") ,strip = False,widget=forms.PasswordInput(attrs = {'autocomplete':'current-password','class':'form-control'}))
    
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        labels = {'disc':"Description"}
        widgets = {'title':forms.TextInput(attrs = {'class':'form-control my-3'}),
                   'disc':forms.Textarea(attrs = {'class':'form-control my-3'}),}