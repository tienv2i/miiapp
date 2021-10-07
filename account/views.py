from django.forms.forms import Form
from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login, logout

from .forms import LoginForm

# Create your views here.
def login_view(request):
    if request.GET.get('next'):
        next = request.GET.get('next')
    elif 'next' in request.POST:
        next = request.POST['next']
    else: 
        next = '/'

    if request.user.is_authenticated:
        form = None
        status = 'login_logged'
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username = username, password = password)
            if user is not None:
                status = 'login_successed'
                auth_login(request, user)
            else:
                status = 'login_failed'
                form = LoginForm()
    else:
        status = 'login_'
        form = LoginForm()
    return render(request, template_name='account/login.html', context= { 
        'form': form, 
        'status': status, 
        'next': next 
    })

def logout_view(request):
    if request.GET.get('next'):
        next = request.GET.get('next')
    else: 
        next = '/'

    if not request.user.is_authenticated:
        status = 'logout_user_do_not_login'
    else:
        logout(request)
        status = 'logout_successed'
    return render(request, template_name='account/logout.html', context = {
        'next': next,
        'status': status
    })