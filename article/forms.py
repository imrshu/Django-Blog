from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from captcha.fields import CaptchaField
from django import forms
from .models import Article


class UserRegistrationForm(UserCreationForm):
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',)


class UserLoginForm(forms.Form):
    username = forms.CharField(label=_("Enter Username"), max_length=150)
    password = forms.CharField(label=_("Enter Password"),
                               widget=forms.PasswordInput(attrs={"class": _("form-control")}))


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('name', 'description', 'image', 'is_private',)
