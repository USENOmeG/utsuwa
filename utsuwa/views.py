import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404

from .forms import *
from .models import *

from django.views.decorators.csrf import csrf_protect

from .utils import *


def home(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username OR password is incorrect')

    return render(request, 'index.html')


def access(reqeust):

    return render(reqeust, 'access.html')


def contact(request):

    return render(request, 'contact.html')


def services(request):

    return render(request, 'services.html')


def news(request):

    return render(request, 'news.html')


def questions(request):

    return render(request, 'questions.html')


def service_business(request):

    return render(request, 'service_business.html')


def service_creative(request):

    return render(request, 'service_creative.html')


def service_tech(request):

    return render(request, 'service_tech.html')


def service_finance(request):

    return render(request, 'service_finance.html')
