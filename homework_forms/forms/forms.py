from django import forms

class ContactForm(forms.Form):
    # задача 1

    name = forms.CharField(label='Ваше имя', max_length=30)
    email = forms.CharField(label='Ваш адрес электронной почты')
    message = forms.CharField(label='Сообщение', widget=forms.Textarea)






