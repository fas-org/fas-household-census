from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def init(request):
    if request.session.get('household') is None:
        return new(request)
    else:
        return edit(request, request.session['household'])


@login_required(login_url='login')
def new(request):
    return render(request, 'householdmembers_section2.html')


@login_required(login_url='login')
def edit(request):
    return render(request, 'householdmembers_section2.html')
