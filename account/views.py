from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from account.forms import AccountAuthenticationForm, AccountUpdateForm
from .models import ResidentChecklist

def logout_view(request):
    logout(request)
    return redirect('easysurf-home')

def login_view(request):
    context = {}
    user = request.user
    if(user.is_authenticated):
        return redirect('home-dashboard')
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if(user):
                login(request, user)
                return redirect('home-dashboard')
    else:
        form = AccountAuthenticationForm()
    context['login_form'] = form
    return render(request, 'account/login.html', context)


def update_account_info(request):
    if not (request.user.is_authenticated):
        return redirect('login')

    context = {}

    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            if ResidentChecklist.objects.filter(resident_id=request.user.id).exists():
                current_resident = ResidentChecklist.objects.filter(resident_id=request.user.id).first()
                current_resident.confirmed_personal_info = True
                current_resident.save()
            else:
                user_checklist = ResidentChecklist(resident = request.user)
                user_checklist.confirmed_personal_info = True
                user_checklist.save()
            return redirect('login')
    else:
        form = AccountUpdateForm (
            initial = {
                "email": request.user.email,
                "username": request.user.username,
                "home_address": request.user.home_address,
                "phone_number": request.user.phone_number,
                "first_name": request.user.first_name,
                "last_name": request.user.last_name,
            }
        )
    context['account_form'] = form
    return render(request, 'account/personal-info-stylized.html', context)
