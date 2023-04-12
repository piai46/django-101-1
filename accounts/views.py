from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render

# Create your views here.


def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/login')
    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def login_view(request):
    if request.user.is_authenticated:
        context = {'user': request.user}
        return render(request, 'accounts/login.html', context)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            context = {'error': 'user or password is invalid'}
            return render(request, 'accounts/login.html', context)
        login(request, user)
        return redirect('/')
    return render(request, 'accounts/login.html', {})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/login/')
    return render(request, 'accounts/logout.html', {})
