from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from user.models import Orders
from series.models import *


class OrderForm(ModelForm):
    class Meta:
        model = Orders
        fields = "__all__"
        widgets = {'productid':forms.TextInput(attrs={"readonly":"readonly"}),

                   }
class OrderUpdateForm(ModelForm):
    class Meta:
        model = Orders
        fields = "__all__"

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields= ['first_name','last_name','username','email','password1']

