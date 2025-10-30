from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm

def index(request):
    if request.method == 'POST':
        
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('reklama')

        return HttpResponse(f'''
            <h2>Вы ввели имя: {name}, вы ввели емайл: {email}, вы ввели сообщение {message}</h2>            
            ''')
    else:
        userform = ContactForm()
        return render(request, 'forms/index.html', {'form':userform})

