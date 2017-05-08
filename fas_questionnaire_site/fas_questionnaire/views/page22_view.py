from django.shortcuts import get_object_or_404, render, redirect
from . import household as household
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from ..models.page22 import InformationOnInvestigators
from ..forms.page22_form import InformationOnInvestigatorsForm
from .common import *


@login_required(login_url='login')
def init(request):
    if request.session.get('household') is None:
        return redirect('household_edit')
    else:
        return edit(request, request.session['household'])


@login_required(login_url='login')
def edit(request, pk):
    request.session['household'] = pk  # TODO: temporary, remove when search functionality is implemented

    if request.method == "POST":
        infoOnInvestigationForm = InformationOnInvestigatorsForm(request.POST, prefix='infoOnInvestigation')

        if save_form(infoOnInvestigationForm, pk) and save_formset(get_comments_formset_to_save(request), Comments, pk, None):
            messages.success(request, 'Data saved successfully')
        return redirect('page22_edit', pk)

    infoOnInvestigation = get_object_or_none(InformationOnInvestigators, pk)
    infoOnInvestigationForm = InformationOnInvestigatorsForm(instance=infoOnInvestigation, prefix='infoOnInvestigation')

    return render(request, 'page22.html', {'infoOnInvestigationForm': infoOnInvestigationForm,
                                          'search_form':get_search_form(),
                                          'comments': get_comments_formset(pk, None)})
