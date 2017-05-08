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
        return redirect('household_edit')
    else:
        return edit(request, request.session['household'])

@login_required(login_url='login')
def edit(request, pk):
    request.session['household'] = pk
    if request.method == "POST":
        current_ownership_formset = formset_factory(OwnershipWellsTubewellsForm, formset=BaseFormSet, extra=1)
        irrigation_means_formset = formset_factory(SpecifiedIrrigationMeansForm, formset=BaseFormSet, extra=1)

        current_ownership_forms = current_ownership_formset(request.POST, prefix='owner')
        irrigation_means_forms = irrigation_means_formset(request.POST, prefix='irrigation')

        if save_formset(current_ownership_forms, OwnershipWellsTubewells, pk) \
                and save_formset(irrigation_means_forms, SpecifiedProductionMeans, pk)\
                and save_formset(get_comments_formset_to_save(request), Comments, pk, 9):
            messages.success(request, 'Data saved successfully')
            return redirect('page9_edit', pk)
        else:
            return render(request, 'page9.html',
                          {'current_ownership_formset': current_ownership_forms,
                           'irrigation_means_formset': irrigation_means_forms,
                           'search_form': get_search_form(),
                           'comments': get_comments_formset(pk, 9)})

    current_ownership_model_formset = modelformset_factory(OwnershipWellsTubewells, form=OwnershipWellsTubewellsForm,
                                                           extra=1)
    current_ownership_result_set = OwnershipWellsTubewells.objects.filter(household=pk)
    current_ownership_formset = current_ownership_model_formset(queryset=current_ownership_result_set, prefix='owner')

    irrigation_means_model_formset = modelformset_factory(SpecifiedProductionMeans, form=SpecifiedIrrigationMeansForm,
                                                          extra=1)
    irrigation_means_result_set = SpecifiedProductionMeans.objects.filter(household=pk, item_type='irrigation')
    irrigation_means_formset = irrigation_means_model_formset(queryset=irrigation_means_result_set, prefix='irrigation')

    return render(request, 'page9.html', {'current_ownership_formset': current_ownership_formset,
                                          'irrigation_means_formset': irrigation_means_formset,
                                          'search_form': get_search_form(),
                                          'comments': get_comments_formset(pk, 9)})