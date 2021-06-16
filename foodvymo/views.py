from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from foodvymo.forms import SignUpForm
from .forms import MerchantForm

def index(request):
    context = {

    }
    return render(request,'foodvymo/index.html',context)


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def addmerchant(request):
    if request.method == 'POST':
        # POST, generate bound form with data from the request
        form = MerchantForm(request.POST)
        # check if it's valid:
        if form.is_valid():
            # Insert into DB
            form.save()
            # redirect to a new URL:
            return render(request,'foodvymo/thankyou.html',{'form':form})
    else:
        # GET, generate unbound (blank) form
        form = MerchantForm()
    return render(request,'foodvymo/addmerchant.html',{'form':form})