from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm, SubscribeForm, PublisherForm, ContactForm2

def work1(request):
    if request.method == 'POST':
        
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        return HttpResponse(f'''
            <pre>
                Вы ввели имя: {name} 
                Вы ввели емайл: {email} 
                Вы ввели сообщение: {message}
            </pre>            
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
            <pre>
                Вы ввели имя: {first_name}
                Вы ввели фамилию: {last_name}
                Вы ввели емайл: {email}
                Ваша подписка на новости: {news}
                Ваша подписка на рекламу: {promo}
            </pre>                        
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
            <pre>
                Вы ввели имя: {name}
                Вы ввели сообщение: {subject} 
                Вы ввели сообщение: {message}
                Вы ввели емайл: {sender}
                Ваше согласие: {agreement}
            </pre>            
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
            <pre>
                Вы ввели имя: {name}
                Вы ввели адрес: {address}
                Вы ввели город: {city} 
                Вы ввели индекс {post_index}
                Вы ввели веб-сайт {website}
            </pre>           
            ''')
    else:
        userform = PublisherForm()
        return render(request, 'forms/index4.html', {'form4':userform})
    
   