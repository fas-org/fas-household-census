from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.forms.formsets import formset_factory, BaseFormSet
from django.forms import modelformset_factory
from ..forms.page_13 import PatternOfAgriculturalLabouringOutForm
from ..models.page_13 import PatternOfAgriculturalLabouringOut
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
        pattern_formset = formset_factory(PatternOfAgriculturalLabouringOutForm, formset=BaseFormSet,extra=1)
        pattern_forms = pattern_formset(request.POST)

        if save_formset(pattern_forms, PatternOfAgriculturalLabouringOut, pk) and save_formset(get_comments_formset_to_save(request), Comments, pk, 13):
            messages.success(request, 'Data saved successfully')
            return redirect('page13_edit', pk)

    pattern_model_formset= modelformset_factory(PatternOfAgriculturalLabouringOut,form=PatternOfAgriculturalLabouringOutForm,extra=1, widgets = get_household_members_as_widget(pk, 'name_of_worker'))
    result_set=PatternOfAgriculturalLabouringOut.objects.filter(household=pk)
    pattern_formset = pattern_model_formset(queryset=result_set)

    return render(request, 'page13.html', {'formset': pattern_formset, 'search_form':get_search_form(), 'comments': get_comments_formset(pk, 13)})
