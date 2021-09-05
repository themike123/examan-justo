from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import HitForm
from .models import Hitman
from accounts.models import Boss
from .utils import functions

@login_required(login_url='/')
def index(request):
    return render(request, 'hits/index.html')


@login_required(login_url='/')
def new(request):

    context = {}
    query_hitman = functions.get_hitmen(request.user)    

    if request.method == 'POST':
        
        form = HitForm(request.POST)
        
        if form.is_valid(): 
            hit = form.save(commit=False)
            hit.creator = request.user
            hit.status = State.objects.get(code=0)#status Assigned
            hit.save()
            messages.add_message(request, messages.SUCCESS, 'Hit was saved')
        else:
            messages.add_message(request, messages.ERROR, 'Error')
    else:
        form = HitForm(initial={'hitman':query_hitman, 'description':'Esta es una prueba'}, user=request.user)
        
    context['form'] = form
    context['hitman'] = query_hitman
    return render(request, 'hits/new.html', context)


@login_required(login_url='/')
def show(request, hit):
    return render(request, 'hits/show.html')

@login_required(login_url='/')
def bulk(request):
    return render(request, 'hits/bulk.html')
