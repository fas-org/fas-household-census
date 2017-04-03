from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import household, introduction, section_3_view


@login_required(login_url='login')
def new(request):
    return render(request, 'home.html')


def update(request, pk):
    householdObj = household.get(pk);
    if householdObj:
        introductionObj = introduction.get(householdObj.id);
        section_3_obj = section_3_view.get(householdObj.id)
    else:
        introductionObj = None
        section_3_obj = None
    return render(request, 'home.html', {
        'householdObj': householdObj,
        'introductionObj': introductionObj,
        'section_3_obj': section_3_obj
    })
