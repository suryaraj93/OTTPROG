from django.forms import ModelForm
from series.models import Language, Movie
from user.models import Orders
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LanguageCreateForm(ModelForm):
    class Meta:
        model = Language
        fields = "__all__"
        widgets = {
            'lang': forms.TextInput(attrs={'class': 'form-control'})
        }


class MovieCreateForm(ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"
        widgets = {"movie_name": forms.TextInput(attrs={'class': 'form-control'}),
                   "genre": forms.TextInput(attrs={"class": "form-control"}),
                   "starring": forms.TextInput(attrs={'class': 'form-control'}),
                   "price": forms.TextInput(attrs={'class': 'form-control'}),
                   # "image": forms.ImageField(attrs={'class': 'form-control'})
                   }


class SearchForm(forms.Form):
    lang = forms.CharField(max_length=120)


