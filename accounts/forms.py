from allauth.account.forms import SignupForm
from django import forms
from .models import CustomUser
from allauth.account.adapter import DefaultAccountAdapter

class CustomSignupForm(SignupForm):
    name = forms.CharField(max_length=255, label='名前')
    
    class Meta:
        model = CustomUser

    def signup(self, request,user):
        user.name = self.cleaned_data['name']
        user.save()
        return user

