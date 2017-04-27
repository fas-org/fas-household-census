from django.shortcuts import get_object_or_404, render, redirect
from . import household as household
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from ..models.page22 import CommentsAndInformationOnInvestigators
from ..forms.page22_form import CommentsAndInformationOnInvestigatorsForm
from .common import *

@login_required(login_url='login')
def init(request):
    if request.session.get('household') is None:
        return new(request)
    else:
        return edit(request, request.session['household'])

@login_required(login_url='login')
def new(request):
    if request.method == "POST":
        investigatorInformationForm = CommentsAndInformationOnInvestigatorsForm(request.POST)
        if investigatorInformationForm.is_valid():
            investigatorInformation = investigatorInformationForm.save(commit=False)
            investigatorInformation.household = household.get(request.session['household'])
            investigatorInformation.save()

            messages.success(request, 'Data saved successfully')
            return redirect('page22_edit', pk=request.session['household'])
    else:
        investigatorInformationForm = CommentsAndInformationOnInvestigatorsForm()
    return render(request, 'page22.html',
                  {'page22_form': investigatorInformationForm, 'search_form': get_search_form()})


@login_required(login_url='login')
def edit(request, pk):
    try:
        request.session['household'] = pk  # TODO: temporary, remove when search functionality is implemented
        investigatorInformation = get_object_or_404(CommentsAndInformationOnInvestigators, household=pk)
        if request.method == "POST":
            form = CommentsAndInformationOnInvestigatorsForm(request.POST, instance=investigatorInformation)
            if form.is_valid():
                investigatorInformation = form.save(commit=False)
                investigatorInformation.save()

                messages.success(request, 'Data saved successfully')

                return redirect('page22_edit', pk=pk)
        else:
            form = CommentsAndInformationOnInvestigatorsForm(instance=investigatorInformation)
        return render(request, 'page22.html',
                      {'page22_form': form,
                       'search_form': get_search_form()
                       })
    except Exception:
        return new(request)


def get(household):
    try:
        investigatorInformation = CommentsAndInformationOnInvestigators.objects.get(household=household)

    except CommentsAndInformationOnInvestigators.DoesNotExist:
        investigatorInformation = None
    return investigatorInformation
