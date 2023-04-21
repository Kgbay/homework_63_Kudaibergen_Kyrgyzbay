from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User, Group

from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField(required=True, label='Логин')
    password = forms.CharField(required=True, label='Пароль',
                               widget=forms.PasswordInput)

    username.widget.attrs.update({'class': 'form-control form-control-lg'})
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
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'})
    )
    username = forms.CharField(
        label='Логин',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'})
    )
    avatar = forms.ImageField(
        label='Аватар',
        required=False,
    )
    phone = forms.IntegerField(
        label='Телефон',
        required=False
    )
    sex = forms.CharField(
        label='Пол',
        widget=forms.Select(),
        required=False
    )
    bio = forms.CharField(
        label='Описание',
        widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
        required=False
    )
    birth_date = forms.DateField(
        label='Дата рождения',
        required=False
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password',
                  'password_confirm', 'first_name',
                  'last_name', 'phone', 'sex', 'bio',
                  'birth_date')
        widgets = {
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
            'avatar': 'аватар',
            'phone': 'телефон',
            'sex': 'Пол',
            'bio': 'Биография',
            'birth_date': 'Дата рождения'
        }

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают')
        if len(str(username).strip()) < 2:
            raise forms.ValidationError('Имя не может быть пустым')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
            Profile.objects.get_or_create(user=user)
        return user


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email')
        labels = {'first_name': 'Имя',
                  'last_name': 'Фамилия',
                  'email': 'Почта'}


class ProfileChangeForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields =('phone', 'sex', 'bio', 'avatar', 'birth_date')

class PasswordChangeForm(forms.ModelForm):
    password = forms.CharField(label="Новый пароль", strip=False, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label="Подтвердите пароль", widget=forms.PasswordInput, strip=False)
    old_password = forms.CharField(label="Старый пароль", strip=False, widget=forms.PasswordInput)


    def clean_password_confirm(self):
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают!')
        return password_confirm

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        if not self.instance.check_password(old_password):
            raise forms.ValidationError('Старый пароль неправильный!')
        return old_password

    def save(self, commit=True):
        user = self.instance
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ['password', 'password_confirm', 'old_password']