from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def index(request):
    return render(request, 'hitmen/index.html')

@login_required(login_url='/')
def show(request,hitmen):
    return render(request, 'hitmen/show.html')
