from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from account.forms import AccountAuthenticationForm

def logout_view(request):
    logout(request)
    return redirect('easysurf-home')

def login_view(request):
    context = {}
    user = request.user
    if(user.is_authenticated):
        return redirect('easysurf-home')
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if(user):
                login(request, user)
                return redirect('easysurf-home')
    else:
        form = AccountAuthenticationForm()
    context['login_form'] = form
    return render(request, 'account/login.html', context)


def update_account_info(request):
    if(request.user.is_authenticated):
        context = {}
        if request.method == "POST":
            fname = request.POST.get("fname")
            print(fname)
        return render(request, "account/personal-info.html", context=context)
    else:
        return redirect('easysurf-home') 
