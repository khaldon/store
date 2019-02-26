from django import forms

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import AbstractUser
from . models import User
class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name','last_name','birthday','gender','email')
 
        # widgets = {
        #         'first_name': forms.TextInput(attrs={'class':'input--style-4'}),
        #         'last_name': forms.TextInput(attrs={'class':'input--style-4'}),
        #         'birthday': forms.TextInput(attrs={'class':'input--style-4 js-datepicker'}),
        #         'email': forms.TextInput(attrs={'class':'input--style-4'}),
        #         'phone_number': forms.TextInput(attrs={'class':'input--style-4'}),
        #         'password1': forms.PasswordInput(attrs={'class':'inpsut--style-4'}),
        #         'password2': forms.PasswordInput(attrs={'class':'inpsut--style-4'}),
        #     }
