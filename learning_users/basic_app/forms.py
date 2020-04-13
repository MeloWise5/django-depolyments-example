from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo

class UserForm(forms.ModelForm):
    #create a password form field
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        #add fields
        fields = ('portfolio_site','profile_pic')


#when creatign a form. You must first make it here.
#then ADD it the views page (from basic_app.forms import UserLoginForm)
#then call this form simply by (user_login_form = UserLoginForm())
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
