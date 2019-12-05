from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.

def home(request):
    return render(request, 'main/index.html')

@login_required
def register(request):
    return render(request, 'main/register.html')


@login_required
def patients(request):
    return render(request, 'main/patients.html')


def rights(request):
    return render(request, 'main/rights.html')
