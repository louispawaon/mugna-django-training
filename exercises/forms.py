from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from exercises.models import Book, Publisher, Author

class PublisherForm(ModelForm):
    class Meta:
        model=Publisher
        fields="__all__"

class BookForm(ModelForm):
    class Meta:
        model=Book
        fields="__all__"

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

class AuthorForm(ModelForm):
    class Meta:
        model=Author
        fields="__all__"
