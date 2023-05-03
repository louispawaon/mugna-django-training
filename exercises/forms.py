from django.forms import ModelForm
from exercises.models import Book, Publisher

class PublisherForm(ModelForm):
    class Meta:
        model=Publisher
        fields="__all__"

class BookForm(ModelForm):
    class Meta:
        model=Book
        fields="__all__"
