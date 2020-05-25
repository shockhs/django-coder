
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required


from .models import CodingElement
from .forms import TextForm
import textAlghoritms

# LOGIN PAGE ROUTE
def login(request):

    if request.user.is_authenticated:
        return redirect('index')
    else: 
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username = username, password = password)

            if user is not None:
                auth_login(request, user)
                return redirect('coder')

        context = {}
        return render(request,'login.html')

# REGISTER PAGE ROUTE
def register(request): 
    form = UserCreationForm()
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Successful registrated')
                return redirect('login')

        context = {'form':form}
        return render(request, 'reg.html', context)

# LOGOUT ROUTE
def logout(request):
    auth_logout(request)
    return redirect('login')


# INDEX PAGE
@login_required(login_url = 'login')
def index(request):
    elements = CodingElement.objects.order_by('id')
    context = {'elements': elements, 'form': TextForm }
    return render(request, 'index.html',context)


# CLEANER ROUTE
@login_required(login_url = 'login')
def cleaner(request):
    CodingElement.objects.all().delete()
    return redirect('index')

# TEXT CODING
@login_required(login_url = 'login')
def textCode(request):

    if request.method == "POST":
        username = request.POST['username']
        textEntered = request.POST['codingText']
        rails = request.POST['rails']
        mode = request.POST['codingMode']
        if int(mode) == 2:
            textEncoded = unicode(textAlghoritms.decode(str(textEntered),int(rails)))
        else:
            textEncoded = unicode(textAlghoritms.encode(str(textEntered),int(rails)))
        new_textElement = CodingElement.objects.create(textEntered = textEntered, textEncoded = textEncoded, rails = rails, username = username)
        new_textElement.save()

    return redirect('index')






