from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from .models import Train


class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class AddTrainForm(forms.ModelForm):
    class Meta:
        model = Train
        fields = ['name', 'source', 'destination', 'total_seats', 'available_seats']

class BookSeatForm(forms.Form):
    train_id = forms.IntegerField()
    seats = forms.IntegerField()

