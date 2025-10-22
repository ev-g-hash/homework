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
    user_list2 = [{'name': 'Дмитрий', 'experience': 9},
                {'name': 'Павел',   'experience': 5},
                {'name': 'Алексей', 'experience': 3},
                {'name': 'Иван',    'experience': 0},
                {'name': 'Денис',   'experience': 2},
                {'name': 'Игорь',   'experience': 7},
                {'name': 'Руслан',  'experience': 1},
                {'name': 'Евгений', 'experience': 4},
                {'name': 'Андрей',  'experience': 2},
                {'name': 'Николай', 'experience': 8}]
    tmpl_name = 'Вася'

    context = {
        'user_name':user_name, 
        'name':name, 
        'age':age, 
        'phone':phone, 'email':email, 
        'profile_data':profile_data, 
        'prof_sps':prof_sps,
        'name_sps':name_sps,
        'experience':experience,
        'user_list':user_list,
        'user_list2':user_list2,
        'tmpl_name':tmpl_name
        }

    return render(request, 'homework/index.html', context)




