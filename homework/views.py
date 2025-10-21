from django.shortcuts import render

def index(request):
    user_name = 'Руслан'
    name = 'Павел'
    age = 45
    phone = '+79234567891'
    email = 'pavel@pavel.com'
    profile_data={'name':'Павел', 'age':45, 'phone':'+79234567891', 'email':'pavel@pavel.com'} 
    context = {'user_name':user_name, 'name':name, 'age':age, 'phone':phone, 'email':email, 'profile_data':profile_data}
    
    return render(request, 'homework/index.html', context)




