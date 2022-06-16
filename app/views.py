from django.shortcuts import render, redirect

# App views
def home(request):
    return render(request, 'index.html')


def next(request):
    return render(request, 'next.html')
