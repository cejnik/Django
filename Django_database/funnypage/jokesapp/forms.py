from django import forms

class JokeForm(forms.Form):
    user_name = forms.CharField(
        label='Vaše jméno', 
        max_length=10, 
        error_messages={
                        'required': 'Jméno nesmí být prázdné',
                        'max_length': 'Prosím vložte kratší jméno'
        },
        widget = forms.TextInput(attrs={'placeholder': 'Jméno'})
    )

    joke_text = forms.CharField(
        label='Váš vtip', 
        widget=forms.Textarea(attrs={'placeholder': 'Váš vtip...'}), 
        max_length=250,

        
    )
    rating = forms.FloatField(
        label='Váš rating', 
        min_value=1, 
        max_value=5,
        widget = forms.NumberInput(attrs={'placeholder': '1-5'})

    )