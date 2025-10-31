from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Ваше имя', max_length=30)
    email = forms.CharField(label='Ваш адрес электронной почты')
    
    