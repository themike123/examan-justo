from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from .forms import UserAgencyForm
from .models import Boss, Hitman, State

def register(request):
    if request.method == 'POST':
        form = UserAgencyForm(request.POST)
        print(request.POST['type_user'])
        if form.is_valid():
            user = form.save()
            if request.POST['type_user'] == 'boss':
                Boss.objects.create(user=user)
            else:
                status = State.objects.get(code='none')
                Hitman.objects.create(user=user,status=status)
            login(request, user)
            messages.add_message(request, messages.SUCCESS, 'User was saved')
            return redirect("hits:index")
        
        messages.add_message(request, messages.ERROR, 'Error')
    else:
        form = UserAgencyForm()
    return render(request, 'accounts/register.html', context={"form":form})


def page_not_found(request):
    return render(request, 'spy_agency/page_not_found.html')

def server_error(request):
    return render(request, 'spy_agency/server_error.html')

def permission_denied(request):
    return render(request, 'spy_agency/permission_denied.html')

def bad_request(request):
    return render(request, 'spy_agency/bad_request.html')
