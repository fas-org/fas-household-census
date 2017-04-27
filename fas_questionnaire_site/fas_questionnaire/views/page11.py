from django.contrib import messages
from django.forms import modelformset_factory
from django.forms.formsets import formset_factory, BaseFormSet
from django.shortcuts import render, redirect

from .common import *
from ..forms.page11 import *
from ..models.page11 import *


@login_required(login_url='login')
def init(request):
    if request.session.get('household') is None:
        return new(request)
    else:
        ownership_result_set = LabourDaysEmployedInAgriculturalOperations.objects.filter(household=request.session.get('household'))
        if len(ownership_result_set) == 0:
            return new(request)
        return edit(request, request.session['household'])


@login_required(login_url='login')
def new(request):
    labour_days_employed_in_agricultural_operations_formset = formset_factory(LabourDaysEmployedInAgriculturalOperationsForm, formset=BaseFormSet, extra=5)
    if request.method == "POST":
        labour_days_employed_in_agricultural_operations_forms = labour_days_employed_in_agricultural_operations_formset(request.POST, prefix='labour_days')
        forms_saved=False
        if labour_days_employed_in_agricultural_operations_forms.is_valid():
            forms_saved = save_forms(request, labour_days_employed_in_agricultural_operations_forms)

        if forms_saved:
            messages.success(request, 'Data saved successfully')
            return redirect('page11_edit', pk=request.session['household'])
        else:
            return render(request, 'page11.html',
                          {'labour_days_employed_in_agricultural_operations_formset': labour_days_employed_in_agricultural_operations_forms,
                           'search_form': get_search_form()})

    return render(request, 'page11.html', {'labour_days_employed_in_agricultural_operations_formset': labour_days_employed_in_agricultural_operations_formset(prefix='labour_days'),
                                           'search_form': get_search_form()})


@login_required(login_url='login')
def edit(request, pk):
    try:
        request.session['household'] = pk
        if request.method == "POST":
            labour_days_employed_in_agricultural_operations_formset = modelformset_factory(LabourDaysEmployedInAgriculturalOperations,
                                                                                           form=LabourDaysEmployedInAgriculturalOperationsForm,
                                                                                           extra=5)

            labour_days_employed_in_agricultural_operations_forms = labour_days_employed_in_agricultural_operations_formset(request.POST, prefix='owner')

            forms_saved = False
            if labour_days_employed_in_agricultural_operations_forms.is_valid():
                forms_saved = save_forms(request, labour_days_employed_in_agricultural_operations_forms)

            if forms_saved:
                messages.success(request, 'Data saved successfully')
            else:
                return render(request, 'page9.html',
                              {'labour_days_employed_in_agricultural_operations_formset': labour_days_employed_in_agricultural_operations_forms,
                               'search_form': get_search_form()})

        labour_days_employed_in_agricultural_operations_formset = modelformset_factory(LabourDaysEmployedInAgriculturalOperations,
                                                                                       form=LabourDaysEmployedInAgriculturalOperationsForm,
                                                                                       extra=5)
        labour_days_employed_in_agricultural_operations_result_set = LabourDaysEmployedInAgriculturalOperations.objects.filter(household=pk)
        labour_days_employed_in_agricultural_operations_formset = labour_days_employed_in_agricultural_operations_formset(queryset=labour_days_employed_in_agricultural_operations_result_set, prefix='owner')

        return render(request, 'page11.html',
                      {'labour_days_employed_in_agricultural_operations_formset': labour_days_employed_in_agricultural_operations_formset,
                       'search_form': get_search_form()})

    except Exception:
        return new(request)
