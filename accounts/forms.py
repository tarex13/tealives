#from turtle import textinput
from django.contrib.auth.forms import UserCreationForm  
try:
    from django.contrib.auth import get_user_model
except ImportError: # django < 1.5
    from django.contrib.auth.models import User
else:
    User = get_user_model()
from django import forms

class LoginForm(forms.Form):
    userid = forms.CharField(
        max_length = 75,
        widget=forms.TextInput(
            attrs={
                "class": "input",
                "placeholder": "Email, Username, or Phone",
                "autocorrect": "off",
                "name": "name",
                "aria-label": "Email, Username, or Phone",
                "id": "teaname",
                "auto-correct": "off",
                "autocomplete": "on",
                "auto-capitalize": "off",
                "oninput": "validateInput()",
            }
        ))
    userpass = forms.CharField(
        max_length = 100,
        widget=forms.PasswordInput(
            attrs={
                "class": "input",
                "placeholder": "Password",
                "name": "pword",
                "id": "teapass",
                "oninput":"validateInput()"

            }
        ))
class SignUpForm(forms.Form): 
    username = forms.CharField(
        max_length = 150,
        widget=forms.TextInput(
        attrs={
            "id": "uname",
            "autocomplete": "off",
            "pattern": "^[a-z](?!.*[_.]{2})[a-z0-9._]{2,29}(?<![_.])$",
            "minlength": "6",
            "required": "true",
            }
            )
        )    
    email = forms.EmailField(
        max_length = 150,
        widget=forms.TextInput(
        attrs={
            "id": "email",
            "autocomplete": "off",
            "minlength": "6",
            "required": "true",
            }
            )
        )
    password = forms.CharField(
        max_length = 150,
        widget = forms.PasswordInput(
            attrs={
                "id":"pass",
                "required":"true",
                "minlength": "8",
                "pattern":"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
                }
            )
        )
        
        #class Meta:  
        #    model = User  
        #    fields = ('username', 'email', 'password')
