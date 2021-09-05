from django.shortcuts import render

def index(request):
    return render(request, 'hits/index.html')

def new(request):
    return render(request, 'hits/new.html')

def show(request, hit):
    return render(request, 'hits/show.html')

def bulk(request):
    return render(request, 'hits/bulk.html')
