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
        # non_agri_result_set = LongTermWorkers.objects.filter(household=request.session.get('household'))
        if len(agri_result_set) == 0:
            return new(request)
        return edit(request, request.session['household'])


@login_required(login_url='login')
def new(request):
    agri_formset = formset_factory(LongTermWorkersForm, formset=BaseFormSet, extra=5)
    # homestead_area_formset = formset_factory(HomesteadAreaForm, formset=BaseFormSet, extra=1)
    if request.method == "POST":
        agri_forms = agri_formset(request.POST, prefix='agri')
        # homestead_area_forms = homestead_area_formset(request.POST, prefix='homestead')
        if agri_forms.is_valid():
            agri_form_saved = save_forms(request, agri_forms)
            # homestead_form_saved = save_forms(request, homestead_area_forms)

        if agri_form_saved:
            messages.success(request, 'Data saved successfully')
            return redirect('page15_edit', pk=request.session['household'])
        else:
            return render(request, 'page15.html',
                          {'agri_formset': agri_forms
                           })

    return render(request, 'page15.html', {'agri_formset': agri_formset(prefix='agri')
                                            })


@login_required(login_url='login')
def edit(request, pk):
    try:
        request.session['household'] = pk  # TODO: temporary, remove when search functionality is implemented
        if request.method == "POST":
            agri_formset = modelformset_factory(LongTermWorkers, form=LongTermWorkersForm, extra=5)
            # homestead_area_formset = modelformset_factory(HomesteadArea, form=HomesteadAreaForm, extra=1)

            agri_forms = agri_formset(request.POST, prefix='agri')
            # homestead_area_forms = homestead_area_formset(request.POST, prefix='homestead')

            if agri_forms.is_valid():
                agri_form_saved = save_forms(request, agri_forms)
                # homestead_form_saved = save_forms(request, homestead_area_forms)

            if agri_form_saved:
                messages.success(request, 'Data saved successfully')
            else:
                return render(request, 'page15.html',
                              {'agri_formset': agri_forms,
                               })

        agri_model_formset = modelformset_factory(LongTermWorkers,
                                                               form=LongTermWorkersForm, extra=5)
        agri_result_set = LongTermWorkers.objects.filter(household=pk)
        agri_formset = agri_model_formset(queryset=agri_result_set, prefix='agri')

        return render(request, 'page15.html', {'agri_formset': agri_formset,
                                              })

    except Exception:
        return new(request)
