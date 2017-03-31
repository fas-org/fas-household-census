from django.shortcuts import render
from . import household, introduction


def new(request):
    return render(request, 'home.html')


def update(request, pk):
    householdObj = household.get(pk);
    if householdObj:
        introductionObj = introduction.get(householdObj.id);
    else :
        introductionObj = None
    return render(request, 'home.html', {
        'householdObj': householdObj,
        'introductionObj': introductionObj
    })