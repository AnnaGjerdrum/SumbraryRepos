from django.contrib.auth.models import User
from django import forms

# user form Class
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, max_length=20)

    #information about the Class
    class Meta:
        model = User
        fields = ['username', 'password']
