from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

def logout_view(request):
    logout(request)
    return redirect('home')

def update_account_info(request):
    context = {}
    return render(request, "account/personal-info.html", context=context)
