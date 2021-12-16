
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

class CustomUserCreationForm(forms.ModelForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('f_name', 'l_name', 'u_name', 'e_mail',)
        # + ('f_name', 'l_name', 'u_name', 'e_mail',)

        widget = {
            'f_name': forms.TextInput(attrs={'class': 'form-control'}),
            'l_name': forms.TextInput(attrs={'class': 'form-control'}),
            'u_name': forms.TextInput(attrs={'class': 'form-control'}),
            'e_mail': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('f_name', 'l_name', 'u_name', 'e_mail',)
        