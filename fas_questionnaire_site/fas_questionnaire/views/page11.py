from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from django.forms.formsets import formset_factory, BaseFormSet
from django.shortcuts import render, redirect

from .common import *
from ..forms.page11 import *
from ..models.page11 import *


@login_required(login_url='login')
def init(request):
    if request.session.get('household') is None:
        return redirect('household_init')
    else:
        return edit(request, request.session['household'])


@login_required(login_url='login')
def edit(request, pk):
    request.session['household'] = pk
    if request.method == "POST":
        labour_days_employed_in_agricultural_operations_formset = formset_factory(LabourDaysEmployedInAgriculturalOperationsForm, formset=BaseFormSet, extra=1)

        labour_days_employed_in_agricultural_operations_forms = labour_days_employed_in_agricultural_operations_formset(request.POST, prefix='owner')

        if save_formset(labour_days_employed_in_agricultural_operations_forms, LabourDaysEmployedInAgriculturalOperations, pk)\
                and save_formset(get_comments_formset_to_save(request), Comments, pk, 11):
            messages.success(request, 'Data saved successfully')
            return redirect('page11_edit', pk)

    labour_days_employed_in_agricultural_operations_formset = modelformset_factory(LabourDaysEmployedInAgriculturalOperations, form=LabourDaysEmployedInAgriculturalOperationsForm, extra=1)
    labour_days_employed_in_agricultural_operations_result_set = LabourDaysEmployedInAgriculturalOperations.objects.filter(household=pk)
    labour_days_employed_in_agricultural_operations_formset = labour_days_employed_in_agricultural_operations_formset(prefix='owner',
                                                          queryset=labour_days_employed_in_agricultural_operations_result_set)

    return render(request, 'page11.html', {
                                            'labour_days_employed_in_agricultural_operations_formset': labour_days_employed_in_agricultural_operations_formset,
                                            'search_form': get_search_form(),
                                            'comments': get_comments_formset(pk, 11)})