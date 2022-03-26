from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,SetPasswordForm
from django.contrib.auth.models import User

from . models import Post

class SignupForm(UserCreationForm):
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'email':'Email','first_name':'First Name','last_name':'Last Name',}
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"class":'form-control'}))
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))


class AddForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','desc']
        labels={'tittle':'Title','desc':'description'}
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'desc':forms.Textarea(attrs={'class':'form-control'})

        }
class SetPassword(SetPasswordForm):
    new_password1=forms.CharField( label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2=forms.CharField(label='Password Confirm',widget=forms.PasswordInput(attrs={'class':'form-control'}))
   
       
