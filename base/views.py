from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'signup-step-1.html', context)
