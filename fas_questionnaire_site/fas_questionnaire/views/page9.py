from django.contrib import messages
from django.forms import modelformset_factory
from django.forms.formsets import formset_factory, BaseFormSet
from django.shortcuts import render, redirect

from .common import *
from ..forms.page9 import *
from ..models.page9 import *


@login_required(login_url='login')
def init(request):
    if request.session.get('household') is None:
        return new(request)
    else:
        ownership_result_set = OwnershipWellsTubewells.objects.filter(household=request.session.get('household'))
        production_means_result_set = SpecifiedProductionMeans.objects.filter(household=request.session.get('household'))
        if len(ownership_result_set) == 0 and len(production_means_result_set) == 0:
            return new(request)
        return edit(request, request.session['household'])


@login_required(login_url='login')
def new(request):
    current_ownership_formset = formset_factory(OwnershipWellsTubewellsForm, formset=BaseFormSet, extra=5)
    production_means_formset = formset_factory(SpecifiedProductionMeansForm, formset=BaseFormSet, extra=5)
    irrigation_means_formset = formset_factory(SpecifiedIrrigationMeansForm, formset=BaseFormSet, extra=2)
    if request.method == "POST":
        current_ownership_forms = current_ownership_formset(request.POST, prefix='owner')
        production_means_forms = production_means_formset(request.POST, prefix='prod')
        irrigation_means_forms = irrigation_means_formset(request.POST, prefix='irrigation')
        current_ownership_forms_saved = False
        production_means_forms_saved = False
        irrigation_means_forms_saved = False
        if current_ownership_forms.is_valid() and production_means_forms.is_valid() and irrigation_means_forms.is_valid():
            current_ownership_forms_saved = save_forms(request, current_ownership_forms)
            production_means_forms_saved = save_forms(request, production_means_forms)
            irrigation_means_forms_saved = save_forms(request, irrigation_means_forms)

        if current_ownership_forms_saved or production_means_forms_saved or irrigation_means_forms_saved:
            messages.success(request, 'Data saved successfully')
            return redirect('page9_edit', pk=request.session['household'])
        else:
            return render(request, 'page9.html',
                          {'current_ownership_formset': current_ownership_forms,
                           'production_means_formset': production_means_forms,
                           'irrigation_means_formset': irrigation_means_forms})

    return render(request, 'page9.html', {'current_ownership_formset': current_ownership_formset(prefix='owner'),
                                                             'production_means_formset': production_means_formset(prefix='prod'),
                                                             'irrigation_means_formset': irrigation_means_formset(prefix='irrigation')})


@login_required(login_url='login')
def edit(request, pk):
    try:
        request.session['household'] = pk
        if request.method == "POST":
            current_ownership_formset = formset_factory(OwnershipWellsTubewellsForm, formset=BaseFormSet, extra=5)
            production_means_formset = formset_factory(SpecifiedProductionMeansForm, formset=BaseFormSet, extra=5)
            irrigation_means_formset = formset_factory(SpecifiedIrrigationMeansForm, formset=BaseFormSet, extra=2)

            current_ownership_forms = current_ownership_formset(request.POST, prefix='owner')
            production_means_forms = production_means_formset(request.POST, prefix='prod')
            irrigation_means_forms = irrigation_means_formset(request.POST, prefix='irrigation')

            current_ownership_forms_saved = False
            production_means_forms_saved = False
            irrigation_means_forms_saved = False
            if current_ownership_forms.is_valid() and production_means_forms.is_valid() and irrigation_means_forms.is_valid():
                OwnershipWellsTubewells.objects.filter(household=pk).delete()
                SpecifiedProductionMeans.objects.filter(household=pk).delete()
                current_ownership_forms_saved = save_forms(request, current_ownership_forms)
                production_means_forms_saved = save_forms(request, production_means_forms)
                irrigation_means_forms_saved = save_forms(request, irrigation_means_forms)

            if current_ownership_forms_saved or production_means_forms_saved or irrigation_means_forms_saved:
                messages.success(request, 'Data saved successfully')
            else:
                return render(request, 'page9.html',
                              {'current_ownership_formset': current_ownership_forms,
                               'production_means_formset': production_means_forms,
                               'irrigation_means_formset': irrigation_means_forms})

        current_ownership_model_formset = modelformset_factory(OwnershipWellsTubewells, form=OwnershipWellsTubewellsForm, extra=5)
        current_ownership_result_set = OwnershipWellsTubewells.objects.filter(household=pk)
        current_ownership_formset = current_ownership_model_formset(queryset=current_ownership_result_set, prefix='owner')

        production_means_model_formset = modelformset_factory(SpecifiedProductionMeans, form=SpecifiedProductionMeansForm, extra=5)
        production_means_result_set = SpecifiedProductionMeans.objects.filter(household=pk)
        production_means_formset = production_means_model_formset(queryset=production_means_result_set, prefix='prod')

        irrigation_means_model_formset = modelformset_factory(SpecifiedProductionMeans, form=SpecifiedIrrigationMeansForm, extra=2)
        irrigation_means_result_set = SpecifiedProductionMeans.objects.filter(household=pk)
        irrigation_means_formset = irrigation_means_model_formset(queryset=irrigation_means_result_set, prefix='irrigation')

        return render(request, 'page9.html', {'current_ownership_formset': current_ownership_formset,
                                                                 'production_means_formset': production_means_formset,
                                                                 'irrigation_means_formset': irrigation_means_formset})

    except Exception:
        return new(request)
