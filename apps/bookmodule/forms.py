from django import forms
from .models import Book
from .models import Student, Address

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'edition', 'price']

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'
        
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
