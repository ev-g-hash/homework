from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm, SubscribeForm, PublisherForm, ContactForm2

def work1(request):
    if request.method == 'POST':
        
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        return HttpResponse(f'''
            <h2>Вы ввели имя: {name}, вы ввели емайл: {email}, вы ввели сообщение {message}</h2>            
            ''')
    else:
        userform = ContactForm()
        return render(request, 'forms/index.html', {'form':userform})

def work2(request):
    if request.method == 'POST':
        
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        news = request.POST.get('news')
        promo = request.POST.get('promo')

        return HttpResponse(f'''
            <h2>Вы ввели имя: {first_name},вы ввели фамилию: {last_name}, вы ввели емайл: {email}, ваша подписка на новости {news}, ваша подписка на рекламу {promo}</h2>            
            ''')
    else:
        userform = SubscribeForm()
        return render(request, 'forms/index2.html', {'form2':userform})
    
def work3(request):
    if request.method == 'POST':
        
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        sender = request.POST.get('sender')
        agreement = request.POST.get('agreement')

        return HttpResponse(f'''
            <h2>Вы ввели имя: {name},вы ввели сообщение: {subject}, 
            вы ввели сообщение: {message}, вы ввели емайл {sender}, ваше согласие {agreement}</h2>            
            ''')
    else:
        userform = ContactForm2()
        return render(request, 'forms/index3.html', {'form3':userform})

def work4(request):
    if request.method == 'POST':
        
        name = request.POST.get('name')
        address = request.POST.get('address')
        city = request.POST.get('city')
        post_index = request.POST.get('post_index')
        website = request.POST.get('website')

        return HttpResponse(f'''
            <h2>Вы ввели имя: {name},вы ввели адрес: {address}, вы ввели город: {city}, 
            вы ввели индекс {post_index}, вы ввели веб-сайт {website}</h2>            
            ''')
    else:
        userform = PublisherForm()
        return render(request, 'forms/index4.html', {'form4':userform})
    
   