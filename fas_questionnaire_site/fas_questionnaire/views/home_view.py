from . import household, introduction
from django.shortcuts import render, redirect


def new(request):
    household_form = household.new(request)
    introduction_form = introduction.new(request)
    if request.session['household'] == 0:
        return render(request, 'home.html',
                      {'household_form': household_form, 'introduction_form': introduction_form})
    else:
        return redirect('home_update', pk=request.session['household'])


def update(request, pk):
    request.session['household'] = pk # when coming from search
    household_form = household.update(request, pk)
    introduction_form = introduction.update(request, pk)
    # keep on adding update views
    return render(request, 'home.html',
                  {'household_form': household_form, 'introduction_form': introduction_form})
