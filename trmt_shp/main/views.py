import requests
import hashlib
import re
import json

from django.shortcuts import render, redirect
from .models import Order, User, LikeBlock, Like
from django.http import JsonResponse

from .forms import OrderForm, UserForm

def home(request):
    return render(request, 'main/index.html')

def love(request):
    return render(request, 'main/love.html')

def send_info(name, phone):
    TOKEN = "5983154594:AAGIF21jGeNH7xe9Y0EQywJa-3O4Kk3PDr0"
    chat_id = "5983154594"
    message = f"Заявка с сайта!\nИмя заказчика: {name}\nТелефон для связи: {phone}"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url).json()

def get_order(request):
    name_error = ''
    email_error = ''
    phone_error = ''
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            name = request.POST.get("name")
            email = request.POST.get("email")
            phone = request.POST.get("phone")
            error = False
            if len(name) > 20 or len(name) < 4 or re.match(r'^[A-ZА-ЯЁ]', ) is None:
                name_error = 'Имя должно начинаться с заглавной буквы и быть от 4 до 20 символом'
                error = True
            if len(email) > 50 or len(email) < 4 or re.match(
                    r'(?=.*[@.])[@.]{4,20}', email) is None:
                email_error = "Проверьте правильность введённой почты"
                error = True
            if len(phone) > 20 or len(phone) < 9 or re.match(
                    r'^[0-9+()- ]', phone) is None:
                phone_error = "Проверьте корректность введенного номера"
                error = True
            if not error:
                f = Order(
                    name = request.POST.get("name"),
                    email=hashlib.sha1(request.POST.get("email").encode('utf-8')).hexdigest(),
                    phone=hashlib.sha1(request.POST.get("phone").encode('utf-8')).hexdigest(),
                )
                f.save()
                send_info(name, phone)
                return redirect('../')
    form = OrderForm()
    data = {
        'form': form,
        'name_error': name_error,
        'email_error': email_error,
        'phone_error': phone_error,
    }
    return render(request, 'main/index.html', data)

def login(request):
    nickname_error = ''
    password_error = ''
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            nickname = request.POST.get("nickname")
            password = request.POST.get("password")
            error = False
            if len(nickname) > 20 or len(nickname) < 4 or re.match(r'^[A-ZА-ЯЁ]', nickname) is None:
                nickname_error = 'Никнейм должен содержать от 4 до 20 символов и начинаться с заглавной буквы'
                error = True
            if len(password) > 20 or len(password) < 6 or re.match(
                    r'(?=.*[0-9])(?=.*[!@#$%^&*])(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z!@#$%^&*]{6,20}', password) is None:
                password_error = "Пароль должен содержать от 6 до 20 символов, хотя бы одно число, " \
                                 "буквы верхнего/нижнего регистра и спецсимвол !@#$%^&*`) "
                error = True
            if not error:
                users = User.objects.all()
                for i in users:
                    if i.nickname == nickname:
                        if i.password == hashlib.sha1(request.POST.get("password").encode('utf-8')).hexdigest():
                            return redirect('../')
                        break
                password_error = "Неправильные имя пользователя или пароль"
    form = UserForm()
    data = {
        'form': form,
        'nickname_error': nickname_error,
        'password_error': password_error,
    }
    return render(request, 'main/login.html', data)


def sign_in(request):
    nickname_error = ''
    password_error = ''
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            nickname = request.POST.get("nickname")
            password = request.POST.get("password")
            password_2 = request.POST.get("pass_2")
            error = False
            if len(nickname) > 20 or len(nickname) < 4 or re.match(r'^[A-ZА-ЯЁ]', nickname) is None:
                nickname_error = 'Никнейм должен содержать от 4 до 20 символов и начинаться с заглавной буквы'
                error = True
            if len(password) > 20 or len(password) < 6 or re.match(r'(?=.*[0-9])(?=.*[!@#$%^&*])(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z!@#$%^&*]{6,20}', password) is None:
                password_error = "Пароль должен содержать от 6 до 20 символов, хотя бы одно число, " \
                                 "буквы верхнего/нижнего регистра и спецсимвол !@#$%^&*`) "
                error = True
            if password != password_2:
                password_error = "Пароли не совпадают"
                error = True
            users = User.objects.all()
            for i in users:
                if i.nickname == nickname:
                    nickname_error = "Такое имя пользователя уже занято"
                    error = True
            if not error:
                f = User(
                    nickname=request.POST.get("nickname"),
                    password=hashlib.sha1(request.POST.get("password").encode('utf-8')).hexdigest()
                )
                f.save()
                return redirect('../')
    form = UserForm()
    data = {
        'form': form,
        'nickname_error': nickname_error,
        'password_error': password_error,
    }
    return render(request, 'main/sign_in.html', data)

def like_block_view(request):
    qs = LikeBlock.liked.all()
    user = request.user

    context = {
        'qs': qs,
        'user': user,
    }
    
    return render(request, 'main/love.html', context)

def like(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = LikeBlock.objects.get(id=post_id)
        
        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)
        
        like, created = Like.objects.get_or_create(user=user, post_id=post_id)

        if not created:
            if like.value == 'Like':
                like.value == 'Unlike'
            else:
                like.value == 'Like'
        like.save()
    return redirect('main:like-like')

def list_users(request):
    users = list(User.objects.all())
    users.sort(key=lambda x: x.points, reverse=True)
    for i in range(len(users)):
        users[i].id = i + 1
    return render(request, 'main/love.html', {'users': users})