from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home:main')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data.get('username'))
            login(request, user)
            return redirect('home:main')

    else:
        form = LoginForm()

    return render(request, 'account/login.html', context={'form': form})


def register_view(request):
    context = {'errors': []}
    if request.user.is_authenticated:
        return redirect('home:main')

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if len(password1) < 8:
            context['errors'].append('رمز عبور باید حداقل 8 کاراکتر باشد!')

        if not any(char.isupper() for char in password1):
            context['errors'].append('رمز عبور باید حداقل یک کاراکتر بزرگ داشته باشد!')

        if not any(char.islower() for char in password1):
            context['errors'].append('رمز عبور باید حداقل یک نویسه کوچک داشته باشد!')

        if not any(char.isdigit() for char in password1):
            context['errors'].append('رمز عبور باید حداقل یک عدد داشته باشد!')

        if password1 != password2:
            context['errors'].append('رمزهای عبور مطابقت ندارند!')

        if not context['errors']:
            user = User.objects.create(username=username, email=email)
            user.set_password(password1)
            user.save()
            login(request, user)
            return redirect('home:main')

    return render(request, 'account/register.html', context)


def logout_view(request):
    logout(request)
    return redirect('home:main')
