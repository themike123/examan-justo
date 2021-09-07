from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from hits.utils import functions
from django.shortcuts import get_object_or_404
from accounts.models import Hitman

@login_required(login_url='/')
def index(request):
    #get_object_or_404(Hitman, pk=1)
    context = { 'hitmen':functions.get_hitmen(request.user) }    
    return render(request, 'hitmen/index.html', context)

@login_required(login_url='/')
def show(request,hitman):
    contex = {'hitman':get_object_or_404(Hitman, pk=hitman)}
    return render(request, 'hitmen/show.html', contex)
