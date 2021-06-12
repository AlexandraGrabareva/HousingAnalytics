from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from .forms import SignUpForm

# def signup(request):
#     return render(request, 'signup.html')
#
#
# def login(request):
#     return render(request, 'login.html')
#
#
# def index(request):
#     return render(request, 'index.html')


def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
