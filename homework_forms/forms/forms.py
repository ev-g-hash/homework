from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Ваше имя', max_length=30)
    email = forms.CharField(label='Ваш адрес электронной почты')
    message = forms.CharField(label='Сообщение', widget=forms.Textarea)


class SubscribeForm(forms.Form):
    first_name = forms.CharField(label='Имя', max_length=30)
    last_name = forms.CharField(label='Фамилия', max_length=30)
    email = forms.CharField(label='E-Mail')
    news = forms.BooleanField(label='Я согласен получать новости', required=False)
    promo = forms.BooleanField(label='Я согласен получать рекламу', required=False)


class ContactForm2(forms.Form):
    name = forms.CharField(label='Отправитель', max_length=30, help_text="Ваши имя и фамилия")
    subject = forms.CharField(label='Сообщение', max_length=200, help_text="Текст сообщения")
    message = forms.CharField(label='Сообщение', widget=forms.Textarea, max_length=200, help_text="Текст сообщения")
    sender = forms.CharField(label='E-Mail', max_length=30, help_text="E-Mail адрес")
    agreement = forms.BooleanField(label='Соглашение', required=False)

class PublisherForm(forms.Form):
    name = forms.CharField(label='Имя', min_length=4, max_length=20, help_text="Введите своё имя")
    address = forms.CharField(label='Адрес', max_length=200, help_text="Введите свой адрес")
    city = forms.CharField(label='Город', max_length=20, help_text="Введите свой город")
    post_index = forms.CharField(label='Почтовый индекс', max_length=20, help_text="Введите свой почтовый индекс")
    website = forms.URLField(label='Сайт', help_text="Введите адрес своего сайта", required=False)

class CarForm(forms.Form):
    model = forms.CharField(label='Модель', initial='undefined')
    brand = forms.CharField(label='Марка', initial='undefined')
    factory_year = forms.IntegerField(label='Год выпуска', initial=2023)
    model_year = forms.IntegerField(label='Модельный год', initial=2022)
    price = forms.IntegerField(label='Цена', initial=0)

# class ContactForm3(forms.Form):
#     name = forms.CharField(label='Имя', help_text="Введите своё имя", error_messages='Ошибка, не введено имя')
#     email = forms.CharField(label='E-Mail', help_text="Введите ваш E-Mail", error_messages='Ошибка, не введён E-Mail')
#     message = forms.CharField(label='Сообщение', widget=forms.Textarea, help_text="Введите сообщение", error_messages='Ошибка, не введено сообщение')
#     promo = forms.BooleanField(label='Подписаться на получение новостных и рекламных рассылок?', required=False)

class ContactForm3(forms.Form):
    name = forms.CharField(label='Имя', help_text="Введите своё имя")
    email = forms.CharField(label='E-Mail', help_text="Введите ваш E-Mail")
    message = forms.CharField(label='Сообщение', widget=forms.Textarea, help_text="Введите сообщение", error_messages={'требуется': 'сообщение'}, attrs={'заполнитель': 'Имя'})
    promo = forms.BooleanField(label='Подписаться на получение новостных и рекламных рассылок?', required=False)




