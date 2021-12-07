from django.db.models.fields import EmailField
from django.shortcuts import render, redirect

from django.contrib import messages
from django.views.decorators.cache import never_cache

from primeEVDev.home.models import Member
from .forms import UserRegistrationForm

# Create your views here.

@never_cache
def home(request):
    return render(request,'homePage/home.html')

@never_cache
def contactUs(request):
    return render(request, 'homePage/contactUs.html')

@never_cache
def aboutUs(request):
    return render(request, 'homePage/aboutUs.html')
@never_cache
def register(request):
    return render(request, 'homePage/info.html')

@never_cache
def registerForm(request):
    template = 'homePage/info.html'

    form = request.POST
    if Member.objects.filter(email=request.POST.get('email')).exists():
        return render(request, template, {'form': form, 'errorMsg': 'Email already exists'})

    else:
        if request.method == "POST":
            gender = False
            if request.POST.get('gender') == "true":
                    gender = True

            member = Member(
                first_name = request.POST.get("fname"),
                last_name = request.POST.get("lname"),
                email = request.POST.get('email'),
                phone_number = request.POST.get('nb'),
                is_male = gender,
                car_brand = request.POST.get('brand'),
                car_type = request.POST.get('carType'),
                battery_range = request.POST.get('bRange'),
                has_card = False,
                license = request.POST.get('license')
            )
            member.save()


"""@never_cache
def signUp(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/SignUp.html', {'form': form})"""

