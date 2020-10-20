from django import forms


class ConnexionForm(forms.Form):
    """ Form to log an User model, this form is passed to the login view"""
    username = forms.CharField(
        label= "username",
        max_length=30,
        required=True
    )
    password = forms.CharField(
        label="password",
        max_length=30,
        required=True
    )

class UserRegisterForm(forms.Form):
    """ Form to create user"""
    pass
    username = forms.CharField(
        label= "username",
        max_length=30,
        required=True
    )
    password = forms.CharField(
        label="password",
        max_length=30,
        widget=forms.PasswordInput,
        required=True
    )
    email = forms.EmailField(
        label="email",
        max_length=30,
        required=True
    )

