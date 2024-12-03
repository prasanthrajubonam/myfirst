
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import LoginForm, SignupForm
from django.db import models


def home(request):
     return render(request, "home.html")
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')  # Replace 'home' with your desired redirect URL
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Replace 'home' with your desired redirect URL
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def destinations(request):
    return render(request, "districts.html") 

def kanakadurga(request):
    return render(request, "kanakadurgatemple.html")
def machilipatnam(request):
    return render(request, "mtm.html")

def kondapalli(request):
    return render(request, "kondapalli.html")

def bhavaniisland(request):
    return render(request, "bhavaniisland.html")

def vijayawada(request):
    return render(request, "vijayawada.html")

def gandhihill(request):
    return render(request, "gandhihill.html")

def kuchipudi(request):
    return render(request, "kuchipudi.html")

def prakasambarrage(request):
    return render(request, "prakasam barrage.html")

def coringawildlife(request):  
    return render(request, "coringawildlife.html")

def papikondalu(request):
    return render(request, "papikondalu.html")

def annavaram(request):
    return render(request, "annavaram.html")

def rajahmundry(request):
    return render(request, "rajahmundry.html")

def draksharamam(request):
    return render(request, "draksharamam.html")

def dindi(request):
    return render(request, "dindi.html")

def maredumilli(request):
    return render(request, "maredumilli.html")

def godavaribridge(request):
    return render(request, "godavari bridge.html")

def kailasagirihills(request):
    return render(request, "kailasagiri hills.html")

def rushikonda(request):
    return render(request, "rushikonda.html")

def lambasingi(request):
    return render(request, "lambasingi.html")

def borracaves(request):
    return render(request, "borra caves.html")

def bheemilibeach(request):
    return render(request, "bheemili beach.html")


def submarinemuseum(request):
    return render(request, "submarine museum.html")


def araku(request):
    return render(request, "araku.html")


def simhachalam(request):
    return render(request, "simhachalam.html")

def lepakshi(request):
    return render(request, "lepakshi.html")

def gootyfort(request):
    return render(request, "gooty fort.html")

def thimmamma(request):
    return render(request, "thimmamma.html")

def hemavathi(request):
    return render(request, "hemavathi temple.html")

def penukonda(request):
    return render(request, "penukonda fort.html")

def klns(request):
    return render(request, "klns.html")

def brs(request):
    return render(request, "brs.html")

def cvs(request):
    return render(request, "cvs.html")

def pedakakani(request):
    return render(request, "pedakakani.html")

def amaravathi(request):
    return render(request, "mahachaitya amaravathi.html")

def chebrole(request):
    return render(request, "chebrole.html")

def mangalagiri(request):
    return render(request, "mangalagiri.html")

def undavalli(request):
    return render(request, "undavalli.html")

def ettipotala(request):
    return render(request, "ettipotala waterfalls.html")

def uppalapadu(request):
    return render(request, "uppalapadu.html")

def dhyana(request):
    return render(request, "dhyana buddha statue.html")

def feedback(request):
    return render(request, "feedback.html")

def feedback1(request):
    return render(request, "feedback1.html")

def gallerypage(request):
    return render(request, "gallery.html")

def contactus(request):
    return render(request, "contact us.html")

def categories(request):
    return render(request, "categories.html")
