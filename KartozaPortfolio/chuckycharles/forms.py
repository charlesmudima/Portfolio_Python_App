from django import forms
from chuckycharles.models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['email','user_name','first_name','last_name']  # Add more fields as needed
