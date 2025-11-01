from django.shortcuts import render
from django.http import HttpResponse

from .forms import ContactForm


def index(request):
    if request.method == 'POST':
        
        name = request.POST.get('name')
        email = request.POST.get('email')        

        return HttpResponse(f'''
            <pre>
                Вы ввели имя: {name} 
                Вы ввели емайл: {email}                 
            </pre>            
        ''')
    else:
        userform = ContactForm()
        return render(request, 'bissnes/index.html', {'form':userform})
