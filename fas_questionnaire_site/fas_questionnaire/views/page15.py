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
        return new(request)
    else:
        agri_result_set = LongTermWorkers.objects.filter(household=request.session.get('household'))
        non_agri_result_set = NonAgricultureWorkers.objects.filter(household=request.session.get('household'))
        if len(agri_result_set) == 0 and non_agri_result_set == 0:
            return new(request)
        return edit(request, request.session['household'])


@login_required(login_url='login')
def new(request):
    agri_formset = formset_factory(LongTermWorkersForm, formset=BaseFormSet, extra=5)
    non_agri_formset = formset_factory(NonAgricultureWorkersForm, formset=BaseFormSet, extra=5)
    if request.method == "POST":
        agri_forms = agri_formset(request.POST, prefix='agri')
        non_agri_forms = non_agri_formset(request.POST, prefix='non_agri')
        agri_form_saved = False
        non_agri_form_saved = False
        if agri_forms.is_valid() and non_agri_forms.is_valid():
            agri_form_saved = save_forms(request, agri_forms)
            non_agri_form_saved = save_forms(request, non_agri_forms)

        if agri_form_saved or non_agri_form_saved:
            messages.success(request, 'Data saved successfully')
            return redirect('page15_edit', pk=request.session['household'])
        else:
            return render(request, 'page15.html',
                          {'agri_formset': agri_forms,
                           'non_agri_formset': non_agri_forms
                           })

    return render(request, 'page15.html', {'agri_formset': agri_formset(prefix='agri'),
                                           'non_agri_formset': non_agri_formset(prefix='non_agri')
                                           })


@login_required(login_url='login')
def edit(request, pk):
    try:
        request.session['household'] = pk  # TODO: temporary, remove when search functionality is implemented
        if request.method == "POST":
            agri_formset = modelformset_factory(LongTermWorkers, form=LongTermWorkersForm, extra=5)
            non_agri_formset = modelformset_factory(NonAgricultureWorkers, form=NonAgricultureWorkersForm, extra=5)

            agri_forms = agri_formset(request.POST, prefix='agri')
            non_agri_forms = non_agri_formset(request.POST, prefix='non_agri')

            agri_form_saved = False
            non_agri_form_saved = False

            if agri_forms.is_valid() and non_agri_forms.is_valid():
                agri_form_saved = save_forms(request, agri_forms)
                non_agri_form_saved = save_forms(request, non_agri_forms)

            if agri_form_saved or non_agri_form_saved:
                messages.success(request, 'Data saved successfully')
            else:
                return render(request, 'page15.html',
                              {'agri_formset': agri_forms,
                               'non_agri_formset': non_agri_forms
                               })

        agri_model_formset = modelformset_factory(LongTermWorkers, form=LongTermWorkersForm, extra=5)
        agri_result_set = LongTermWorkers.objects.filter(household=pk)
        agri_formset = agri_model_formset(queryset=agri_result_set, prefix='agri')

        non_agri_model_formset = modelformset_factory(NonAgricultureWorkers, form=NonAgricultureWorkersForm, extra=5)
        non_agri_result_set = NonAgricultureWorkers.objects.filter(household=pk)
        non_agri_formset = non_agri_model_formset(queryset=non_agri_result_set, prefix='non_agri')

        return render(request, 'page15.html', {'agri_formset': agri_formset,
                                               'non_agri_formset': non_agri_formset
                                               })

    except Exception:
        return new(request)
