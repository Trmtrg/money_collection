from django.forms import ModelForm, TextInput, FileInput, NumberInput

from .models import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['Title', 'Image', 'Image_two', 'Country', 'Metal', 'Year', 'Nominal', 'Text']

        widgets = {
            "Title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
            "Image": FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фото лицевой стороны монеты',
                'accept': 'image/png'
            }),
            "Image_two": FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фото обратной стороны монеты',
                'accept': 'image/png'
            }),
            "Country": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Страна'
            }),
            "Metal": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Метал'
            }),
            "Year": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Год выпуска монеты'
            }),
            "Nominal": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номинал'
            }),
            "Text": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            }),

        }
