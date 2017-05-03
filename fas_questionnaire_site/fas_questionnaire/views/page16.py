from django.contrib import messages
from django.forms import modelformset_factory
from django.forms.formsets import formset_factory, BaseFormSet
from django.shortcuts import get_object_or_404, render, redirect

from .common import *
from ..forms.page16 import *
from ..models.page16 import *

@login_required(login_url='login')
def init(request):
    if request.session.get('household') is None:
        return redirect('household_init')
    else:
        return edit(request, request.session['household'])


@login_required(login_url='login')
def edit(request, pk):
    request.session['household'] = pk
    freedom_of_employment_questions = get_object_or_none(FreedomOfEmploymentQuestions, household_id=pk)
    if request.method == "POST":
        income_from_state_formset = formset_factory(IncomeFromStateAndCommonPropertyResourcesForm, formset=BaseFormSet, extra=5)
        aggri_or_non_aggri_labour_service_formset = formset_factory(AgriculturalOrNonAgriculturalLabourServicesForm,
                                                                         formset=BaseFormSet,
                                                                         extra=5)

        income_from_state_forms = income_from_state_formset(request.POST, prefix='income_from_state')
        aggri_or_non_aggri_labour_service_forms = aggri_or_non_aggri_labour_service_formset(request.POST,
                                                                                            prefix='aggri_or_non_aggri_labour_service')
        freedom_of_employment_questions_form = FreedomOfEmploymentQuestionsForm(request.POST,
                                                                                instance=freedom_of_employment_questions)

        if save_formset(income_from_state_forms, IncomeFromStateAndCommonPropertyResources, pk) and save_formset(aggri_or_non_aggri_labour_service_forms,
                                                                                                                 AgriculturalOrNonAgriculturalLabourServices,
                                                                                      pk) \
                and save_form(freedom_of_employment_questions_form, pk):
            messages.success(request, 'Data saved successfully')
            return redirect('page16_edit', pk)

    income_from_state_model_formset = modelformset_factory(IncomeFromStateAndCommonPropertyResources,
                                                           form=IncomeFromStateAndCommonPropertyResourcesForm, extra=5)
    income_from_state_result_set = IncomeFromStateAndCommonPropertyResources.objects.filter(household=pk)
    income_from_state_formset = income_from_state_model_formset(queryset=income_from_state_result_set,
                                                                prefix='income_from_state')

    aggri_or_non_aggri_labour_service_model_formset = modelformset_factory(AgriculturalOrNonAgriculturalLabourServices,
                                                                           form=AgriculturalOrNonAgriculturalLabourServicesForm,
                                                                           extra=5)
    aggri_or_non_aggri_labour_service_result_set = AgriculturalOrNonAgriculturalLabourServices.objects.filter(
        household=pk)
    aggri_or_non_aggri_labour_service_formset = aggri_or_non_aggri_labour_service_model_formset(
        queryset=aggri_or_non_aggri_labour_service_result_set,
        prefix='aggri_or_non_aggri_labour_service')

    freedom_of_employment_questions_form = FreedomOfEmploymentQuestionsForm(instance=freedom_of_employment_questions)

    return render(request, 'page16.html', {'income_from_state_formset': income_from_state_formset,
                                           'aggri_or_non_aggri_labour_service_formset': aggri_or_non_aggri_labour_service_formset,
                                           'freedom_of_employment_questions_form': freedom_of_employment_questions_form,
                                           'search_form': get_search_form()})