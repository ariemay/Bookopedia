from django import forms
from .models import Book, Type


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'number_of_pages', 'type_of_book', 'slug', 'image_file')

class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ('type_name', 'slug')
