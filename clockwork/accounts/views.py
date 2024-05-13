from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Account
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import RegistrationForm


@login_required
def account(request):
    info = request.user
    if info.is_staff:
        return redirect('/admin/')
    else:
        return render(request, 'accounts/account.html', {'account': info})


def select_view(request):
    if request.user.is_authenticated:
        return redirect('accounts:account')
    else:
        return render(request,'registration/select.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            raw_password = form.cleaned_data.get('password1')
            user.set_password(raw_password)
            user.save()
            print("Пароль:", raw_password)

            # Проверяем, что учетные данные пользователя правильно передаются
            print("Email пользователя:", user.email)
            print("Пользователь:", user.username)

            # Попробуем аутентифицировать пользователя после регистрации
            user = authenticate(request, username=user.username, password=raw_password)
            if user is not None:
                auth_login(request, user)  # Используем auth_login для аутентификации пользователя
                return redirect(reverse('showcase:catalog'))
            else:
                print('Аутентификация не удалась')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect(reverse('showcase:catalog'))
            else:
                print(username, password)
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect(reverse('showcase:catalog'))

