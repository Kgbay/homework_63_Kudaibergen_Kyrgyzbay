from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from .models import Profile


class LoginForm(forms.Form):
    login = forms.CharField(required=True, label='Логин')
    password = forms.CharField(required=True, label='Пароль',
                               widget=forms.PasswordInput)

    login.widget.attrs.update({'class': 'form-control form-control-lg'})
    password.widget.attrs.update({'class': 'form-control form-control-lg'})


class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(
        label='Пароль',
        strip=False,
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'})
    )
    password_confirm = forms.CharField(
        label='Подтвердите пароль',
        strip=False,
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'})
    )
    email = forms.CharField(
        label='Электронная почта',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'})
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password',
                  'password_confirm', 'first_name',
                  'last_name')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control form-control-lg'})
        }
        labels = {
            'username': 'Логин',
            'email': 'Электронная почта',
            'password': 'Пароль',
            'password_confirm': 'Подтвердите пароль',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают')
        if len(str(username).strip()) < 2:
            raise forms.ValidationError('Имя не может быть пустым')
        if first_name == last_name:
            raise forms.ValidationError('Имя и фамилия не могут быть одинаковыми')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email')
        labels = {'first_name': 'Имя',
                  'username': 'Логин',
                  'last_name': 'Фамилия',
                  'email': 'Почта'}


class ProfileChangeForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields =('phone', 'sex', 'bio', 'avatar', 'birth_date')