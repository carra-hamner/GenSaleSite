from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import SignUpForm, ListingForm
from .models import ListItem


def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST, auto_id="register_%s")
        if signup_form.is_valid() and 'signup_btn' in request.POST:
            user = signup_form.save()
            user.refresh_from_db()
            # load the profile instance created by the signal
            user.save()
            raw_password = signup_form.cleaned_data.get('password1')
            user.save()
            # login user after signing up
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect(reverse('TheSaleSite:listing'))
    else:
        signup_form = SignUpForm()

    return render(request, 'signup.html', {'signup_form': signup_form})


def listing(request):
    context = {}
    if request.method == 'POST':
        list_form = ListingForm(request.POST)
        if list_form.is_valid():
            list_item = ListItem()
            list_item.name = list_form.cleaned_data['name']
            list_item.contact_email = list_form.cleaned_data['contact_email']
            list_item.list_option = list_form.cleaned_data['list_option']
            list_item.price = list_form.cleaned_data['price']
            list_item.description = list_form.cleaned_data['description']
            list_item.save()
            return HttpResponseRedirect(reverse('TheSaleSite:products'))
    else:
        if request.user.is_authenticated:
            context = {'list_form': ListingForm()}
        else:
            return HttpResponseRedirect(reverse('TheSaleSite:signup'))
    return render(request, 'listing.html', context)


def products(request):
    all_listing = ListItem.objects.all()
    return render(request, 'products.html', {'all_listing': all_listing})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('TheSaleSite:index'))


def login_view(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid() and 'login_btn' in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
            else:
                messages.info(request, 'username or password is incorrect')
            return HttpResponseRedirect(reverse('TheSaleSite:listing'))
    else:
        login_form = AuthenticationForm(data=request.POST)
    return render(request, 'login.html', {'login_form': login_form})


def cart(request):
    return render(request, 'cart.html')


def signup_or_login_redirect(request):
    return render(request, 'signup_or_login_redirect.html')
