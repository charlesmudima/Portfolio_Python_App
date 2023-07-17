from django import forms
from chuckycharles.models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['email', 'user_name', 'first_name', 'last_name'
                    , 'password','address','phone_number', 'about', 'is_staff', 'is_active'] # Add more fields as needed


# update profile form
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_number', 'address', 'about']