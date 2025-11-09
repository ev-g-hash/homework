from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Ваше имя', max_length=30)
    email = forms.CharField(label='Ваш адрес электронной почты', max_length=100)
    phone = forms.CharField(label='Ваш телефон', max_length=30)
    message = forms.CharField(label='Сообщение', max_length=200)

