from django.shortcuts import render

def index(request):
    user_name = 'Руслан'
    name = 'Павел'
    age = 45
    phone = '+79234567891'
    email = 'pavel@pavel.com'
    profile_data={'name':'Павел', 'age':45, 'phone':'+79234567891', 'email':'pavel@pavel.com'}
    prof_sps=['Павел', 45, '+79234567891', 'pavel@pavel.com'] 
    name_sps = ['Павел', 'Алексей']
    experience = [3, 6]
    user_list = ['Игорь', 'Андрей', 'Дмитрий', 'Алексей', 'Николай', 'Евгений', 'Иван', 'Павел']


    context = {
        'user_name':user_name, 
        'name':name, 
        'age':age, 
        'phone':phone, 'email':email, 
        'profile_data':profile_data, 
        'prof_sps':prof_sps,
        'name_sps':name_sps,
        'experience':experience,
        'user_list':user_list
        }

    return render(request, 'homework/index.html', context)





