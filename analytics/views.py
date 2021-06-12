from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from .models import Developer, House
from django.shortcuts import render
from .filters import HouseFilter


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


def developers(request):
    developer_list = Developer.objects.all()
    return render(request, 'developers.html', {'developers': developer_list})


def houses(request):
    house_list = House.objects.all()
    return render(request, 'houses.html', {'houses': house_list})


def search(request):
    house_list = House.objects.all()
    house_filter = HouseFilter(request.GET, queryset=house_list)

    return render(request, 'search.html', {'filter': house_filter})
