from django import forms
from .models import UserProfile
from django.contrib.auth.models import User

class addUserProfileForm(forms.ModelForm):
    
    class Meta:
        model = UserProfile
        fields = '__all__'
        
class addUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        
class levelForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['level']

