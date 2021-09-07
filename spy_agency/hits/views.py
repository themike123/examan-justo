from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from .forms import HitForm
from accounts.models import State
from .models import Hit
from .utils import functions
from django.shortcuts import get_object_or_404
from django.http import Http404


@login_required(login_url='/')
def index(request):
    context = { 'hits':functions.get_hits(request.user) }    
    return render(request, 'hits/index.html', context)


@login_required(login_url='/')
#@permission_required('hits.add_hit', login_url='/hits/')
def new(request):

    context = {}
    query_hitman = functions.get_hitmen(request.user)    

    if request.method == 'POST':
        
        form = HitForm(request.POST,user=request.user)
        
        if form.is_valid(): 
            hit = form.save(commit=False)
            hit.creator = request.user
            hit.status = State.objects.get(code=0)#status Assigned
            hit.save()
            messages.add_message(request, messages.SUCCESS, 'Hit was saved')
        else:
            messages.add_message(request, messages.ERROR, 'Error')
    else:
        form = HitForm(user=request.user)
        
    context['form'] = form
    context['hitman'] = query_hitman
    return render(request, 'hits/new.html', context)


@login_required(login_url='/')
def show(request, hit):
    
    print(get_object_or_404(Hit, pk=hit) )
    
    try:
        
        contex = {'hit':Hit.objects.get(id=hit)}

        #if functions.is_hitman(request.user):
        #    pass
        #elif functions.is_boss(request.user):
        #    pass
        #else:
        #    pass


        return render(request, 'hits/show.html', contex)
    except Exception as err: #return other view        
        raise Http404(err)
        print(err)
        print("error")        
    except Hit.DoesNotExist as err: #return other view
        print(err)
    

@login_required(login_url='/')
def bulk(request):
    return render(request, 'hits/bulk.html')
