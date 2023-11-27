# myapp/forms.py
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    usertype = forms.ChoiceField(choices=[('patient', 'Patient'), ('doctor', 'Doctor')])  # Add this line

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'address_line1', 'city', 'state', 'pincode']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    usertype = forms.ChoiceField(choices=[('patient', 'Patient'), ('doctor', 'Doctor')])  # Add this line
