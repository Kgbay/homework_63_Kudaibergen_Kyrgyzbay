from django import forms
from django.core.exceptions import ValidationError

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('desc', 'point', 'location', 'image')
        widgets = {
            'desc': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'point': forms.TextInput(attrs={'class': 'form-control form-control-lg'})
        }
        labels = {
            'desc': 'Описание поста',
            'image': 'Изображения',
            'point': 'Местоположения',
            'location': 'Карта',
            'user': 'Пользователь'
        }

    def clean(self):
        cleaned_data = super().clean()
        if len(cleaned_data['desc']) < 2:
            raise ValidationError("Длина поле должна быть больше двух символов")
        return cleaned_data


class SearchForm(forms.Form):
    search = forms.CharField(max_length=20, required=False, label='')
