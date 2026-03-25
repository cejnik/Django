from django import forms

class BookForm(forms.Form):
    book_name =forms.CharField(max_length=255, required=True, label='Název knihy')
    book_price = forms.IntegerField(min_value=1, max_value=10000, required=True, label='Cena')
    
