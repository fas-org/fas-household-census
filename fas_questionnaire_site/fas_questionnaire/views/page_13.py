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


@login_required(login_url='login')
def init(request):
    if request.session.get('household') is None:
        return new(request)
    else:
        return edit(request, request.session['household'])


@login_required(login_url='login')
def new(request):
    pattern_formset= formset_factory(PatternOfAgriculturalLabouringOutForm,formset=BaseFormSet,extra=5)
    if request.method == "POST":
        pattern_forms=pattern_formset(request.POST)
        if pattern_forms.is_valid():
            active_ids = []
            for form in pattern_forms:
                id = form.data[form.prefix+'-id']
                if form.is_valid() and form.has_changed():
                    record = form.save(commit=False)
                    if id:
                        record.id = int(id)
                    record.household = Household.objects.get(pk=request.session['household'])
                    record.save()
                    active_ids.append(record.id)
                else:
                    if id:
                        active_ids.append(int(id))

        return redirect('page_13_edit', pk=request.session['household'])

    return render(request,'page_13.html',{'formset': pattern_formset})


@login_required(login_url='login')
def edit(request, pk):
    if request.method == 'POST':
        pattern_formset = formset_factory(PatternOfAgriculturalLabouringOutForm, formset=BaseFormSet,extra=5)
        pattern_forms = pattern_formset(request.POST)

        if pattern_forms.is_valid():
            active_ids = []
            for form in pattern_forms:
                id = form.data[form.prefix+'-id']
                if form.is_valid and form.has_changed():
                    record=form.save(commit=False)
                    if id:
                        record.id = int(id)
                    record.household=Household.objects.get(pk=request.session['household'])
                    record.save()
                    active_ids.append(record.id)
                else:
                    if id:
                        active_ids.append(int(id))

            all_ids = list(PatternOfAgriculturalLabouringOut.objects.filter(household=pk).values_list('id',flat=True))
            PatternOfAgriculturalLabouringOut.objects.filter(id__in=[ x for x in all_ids if x not in active_ids]).delete()

    pattern_model_formset= modelformset_factory(PatternOfAgriculturalLabouringOut,form=PatternOfAgriculturalLabouringOutForm,extra=5, widgets={ 'name_of_worker' : forms.Select(choices=[ (c.id, c.name) for c in HouseholdMembers.objects.filter(household=pk)])})
    result_set=PatternOfAgriculturalLabouringOut.objects.filter(household=pk)
    pattern_formset = pattern_model_formset(queryset=result_set)
    return render(request,'page_13.html',{'formset': pattern_formset})
