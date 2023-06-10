from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from account.forms import LoginForm, EditUserForm


def login_page(request):
    if request.user.is_authenticated == True:
        return redirect('home:home')

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data.get('username'))
            login(request, user)
            return redirect("home:home")
    else:
        form = LoginForm()
    return render(request, "account/login.html", context={'form': form})


def user_edit(request):
    user = request.user
    form = EditUserForm(instance=user)
    if request.method == 'POST':
        form = EditUserForm(instance=user, data=request.POST)
        if form.is_valid():
            form.save()
    return render(request, "account/edit.html", context={'form': form})


def user_logout(request):
    logout(request)
    return redirect('home:home')


def user_register(request):
    context = {'Errors': []}
    if request.user.is_authenticated == True:
        return redirect('home:home')

    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            context['Errors'].append(' Password is not same')
            return render(request, 'account/register.html', context)

        elif User.objects.get(username=username):
            context['Errors'].append(' this user is exist')
            return render(request, 'account/register.html', context)
        user = User.objects.create(username=username, password=password1, email=email)
        login(request, user)
        return redirect('home:home')

    return render(request, 'account/register.html', context)
