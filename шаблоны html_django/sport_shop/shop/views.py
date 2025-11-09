from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm

def index(request):
    return render(request, 'shop/index.html')

def aboutas(request):
    return render(request, 'shop/aboutas.html')

def readmore(request):
    return render(request, 'shop/readmore.html')

def forms(request):
    if request.method == 'POST':
        
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        return HttpResponse(f'''
            <pre>
                Вы ввели следующие данные
                Вы ввели имя: {name} 
                Вы ввели емайл: {email} 
                Вы ввели телефон: {phone} 
                Вы ввели сообщение: {message}
                Ожидайте в ближайшее время мы с вами свяжемся!
            </pre>            
        ''')
    else:
        userform = ContactForm()
        return render(request, 'shop/forms.html', {'form':userform})
    
def forms2(request):
    return render(request, 'shop/forms2.html')