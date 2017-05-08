from ..forms.page15 import *
from ..models.page15 import *
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.forms.formsets import formset_factory, BaseFormSet
from django.forms import modelformset_factory
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
    if request.method == "POST":
        agri_formset = formset_factory(LongTermWorkersForm, formset=BaseFormSet, extra=1)
        non_agri_formset = formset_factory(NonAgricultureWorkersForm, formset=BaseFormSet, extra=1)

        agri_forms = agri_formset(request.POST, prefix='agri')
        non_agri_forms = non_agri_formset(request.POST, prefix='non_agri')

        if save_formset(agri_forms, LongTermWorkers, pk) \
                and save_formset(non_agri_forms, NonAgricultureWorkers, pk) and save_formset(get_comments_formset_to_save(request), Comments, pk, 15):
            messages.success(request, 'Data saved successfully')
            return redirect('page15_edit', pk)

    agri_model_formset = modelformset_factory(LongTermWorkers, form=LongTermWorkersForm, extra=1)
    agri_result_set = LongTermWorkers.objects.filter(household=pk)
    agri_formset = agri_model_formset(queryset=agri_result_set, prefix='agri')

    non_agri_model_formset = modelformset_factory(NonAgricultureWorkers, form=NonAgricultureWorkersForm, extra=1)
    non_agri_result_set = NonAgricultureWorkers.objects.filter(household=pk)
    non_agri_formset = non_agri_model_formset(queryset=non_agri_result_set, prefix='non_agri')

    return render(request, 'page15.html', {'agri_formset': agri_formset,
                                           'non_agri_formset': non_agri_formset,
                                           'search_form': get_search_form(),
                                           'comments': get_comments_formset(pk, 15)})