from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.forms.formsets import formset_factory, BaseFormSet
from django.forms import modelformset_factory

from fas_questionnaire.models.page1 import HouseholdMembers
from ..forms.page_13 import PatternOfAgriculturalLabouringOutForm
from ..models.page_13 import PatternOfAgriculturalLabouringOut
from ..models.household_models import Household
from django import forms
from .common import *

@login_required(login_url='login')
def init(request):
    if request.session.get('household') is None:
        return redirect('household_init')
    else:
        return edit(request, request.session['household'])

@login_required(login_url='login')
def edit(request, pk):
    request.session['household'] = pk
    if request.method == 'POST':
        pattern_formset = formset_factory(PatternOfAgriculturalLabouringOutForm, formset=BaseFormSet,extra=5)
        pattern_forms = pattern_formset(request.POST)

        if save_formset(pattern_forms, PatternOfAgriculturalLabouringOut, pk):
            messages.success(request, 'Data saved successfully')
            return redirect('page13_edit', pk)

    pattern_model_formset= modelformset_factory(PatternOfAgriculturalLabouringOut,form=PatternOfAgriculturalLabouringOutForm,extra=5, widgets={ 'name_of_worker' : forms.Select(choices=[ (c.id, c.name) for c in HouseholdMembers.objects.filter(household=pk)])})
    result_set=PatternOfAgriculturalLabouringOut.objects.filter(household=pk)
    pattern_formset = pattern_model_formset(queryset=result_set)
    return render(request, 'page13.html', {'formset': pattern_formset, 'search_form':get_search_form()})
