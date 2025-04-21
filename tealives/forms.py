from django import forms


#class LoginForm(forms.Form):
#    userid = forms.CharField(
#        max_length = 75,
#        widget=forms.TextInput(
#            attrs={
#                "class": "input",
#                "placeholder": "Email, Username, or Phone",
#                "autocorrect": "off",
#                "name": "name",
#                "aria-label": "Email, Username, or Phone",
#                "id": "teaname",
#                "auto-correct": "off",
#                "autocomplete": "on",
#                "auto-capitalize": "off",
#                "oninput": "hbjhb()",
#            }
#        ))
#    userpass = forms.CharField(
#        max_length = 100,
#        widget=forms.PasswordInput(
#            attrs={
#                "class": "input",
#                "placeholder": "Password",
#                "name": "pword",
#                "id": "teapass",
#                "oninput":"hbjhb()"

#            }
#        ))
#class RegistrationForm(forms.Form):
#    userid = forms.CharField(
#        max_length = 75,
#        widget=forms.TextInput(
#            attrs={
#                "class": "input",
#                "placeholder": "Email or Phone",
#                "autocorrect": "off",
#                "name": "id",
#                "aria-label": "Email, Username, or Phone",
#                "id": "teaname",
#                "auto-correct": "off",
#                "autocomplete": "on",
#                "auto-capitalize": "off",
#                "onchange": "hbjhb()",
#            }
#        ))
#    userpass = forms.CharField(
#        max_length = 100,
#        widget=forms.PasswordInput(
#            attrs={
#                "class": "input",
#                "placeholder": "Password",
#                "name": "pword",
#                "id": "teapass"
#            }
#        ))
#    username = forms.CharField(
#        max_length = 75,
#        widget=forms.TextInput(
#            attrs={
#                "class": "input",
#                "placeholder": "Username",
#                "autocorrect": "off",
#                "name": "username",
#                "aria-label": "Username",
#                "id": "uname",
#                "auto-correct": "off",
#                "autocomplete": "on",
#                "auto-capitalize": "off",
#                "onchange": "hbjhb()",
#            }
#        ))