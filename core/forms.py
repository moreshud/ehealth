from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm

from .models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=250,
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control mb-2", "placeholder": "Your firstname"}
        ),
        required=True,
    )
    last_name = forms.CharField(
        max_length=250,
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control mb-2", "placeholder": "Your lastname"}
        ),
        required=True,
    )

    gender = forms.ChoiceField(
        label="",
        choices=User.GENDER_CHOICES,
        widget=forms.Select(
            attrs={
                "class": "form-control mb-2",
            }
        ),
        required=True,
    )

    email = forms.EmailField(
        label="",
        widget=forms.EmailInput(
            attrs={"class": "form-control mb-2", "placeholder": "mark@example.com"}
        ),
        required=True,
    )

    password1 = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={"class": "form-control mb-2", "placeholder": "Your password"}
        ),
        required=True,
    )

    password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={"class": "form-control mb-2", "placeholder": "Re-type your password"}
        ),
        required=True,
    )

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "gender",
            "email",
            "password1",
            "password2",
        )

    def clean_email(self):
        email = self.cleaned_data["email"].lower()

        if User.objects.filter(email=email):
            raise ValidationError("This email address already exists.")
        return email


class SignInForm(AuthenticationForm):
    username = forms.EmailField(
        label="",
        widget=forms.EmailInput(
            attrs={"class": "form-control mb-2", "placeholder": "mark@example.com"}
        ),
        required=True,
    )
    # username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={"class": "form-control mb-2", "placeholder": "Your password"}
        ),
        required=True,
    )

    def __init__(self, *args, **kwargs):
        super(SignInForm, self).__init__(*args, **kwargs)
