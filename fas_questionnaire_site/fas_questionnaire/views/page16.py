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
        return new(request)
    else:
        income_from_state_result_set = IncomeFromStateAndCommonPropertyResources.objects.filter(household=request.session.get('household'))
        aggri_or_non_aggri_labour_service_result_set = AgriculturalOrNonAgriculturalLabourServices.objects.filter(
            household=request.session.get('household'))
        freedom_of_employment_questions_result_set = FreedomOfEmploymentQuestions.objects.filter(household=request.session.get('household'))
        if len(income_from_state_result_set) == 0 and len(aggri_or_non_aggri_labour_service_result_set) == 0 and len(freedom_of_employment_questions_result_set) == 0:
            return new(request)
        return edit(request, request.session['household'])


@login_required(login_url='login')
def new(request):
    income_from_state_formset = formset_factory(IncomeFromStateAndCommonPropertyResourcesForm, formset=BaseFormSet, extra=5)
    aggri_or_non_aggri_labour_service_formset = formset_factory(AgriculturalOrNonAgriculturalLabourServicesForm, formset=BaseFormSet,
                                                                extra=5)
    freedom_of_employment_questions_form = FreedomOfEmploymentQuestionsForm()

    if request.method == "POST":
        income_from_state_forms = income_from_state_formset(request.POST, prefix='income_from_state')
        aggri_or_non_aggri_labour_service_forms = aggri_or_non_aggri_labour_service_formset(request.POST,
                                                                                            prefix='aggri_or_non_aggri_labour_service')
        freedom_of_employment_questions_form = FreedomOfEmploymentQuestionsForm(request.POST)

        income_from_state_form_saved = False
        aggri_or_non_aggri_labour_service_form_saved = False
        freedom_of_employment_questions_form_saved = False

        if income_from_state_forms.is_valid() and aggri_or_non_aggri_labour_service_forms.is_valid() and freedom_of_employment_questions_form.is_valid():
            income_from_state_form_saved = save_forms(request, income_from_state_forms)
            aggri_or_non_aggri_labour_service_form_saved = save_forms(request, aggri_or_non_aggri_labour_service_forms)
            freedom_of_employment_questions_form_saved = save_form_with_no_has_change(request, freedom_of_employment_questions_form)

        if income_from_state_form_saved and aggri_or_non_aggri_labour_service_form_saved and freedom_of_employment_questions_form_saved:
            messages.success(request, 'Data saved successfully')
            return redirect('page16_edit', pk=request.session['household'])
        else:
            return render(request, 'page16.html',
                          {'income_from_state_formset': income_from_state_forms,
                           'aggri_or_non_aggri_labour_service_formset': aggri_or_non_aggri_labour_service_forms,
                           'freedom_of_employment_questions_form': freedom_of_employment_questions_form})

    return render(request, 'page16.html', {'income_from_state_formset': income_from_state_formset(prefix='income_from_state'),
                                           'aggri_or_non_aggri_labour_service_formset': aggri_or_non_aggri_labour_service_formset(
                                               prefix='aggri_or_non_aggri_labour_service'),
                                           'freedom_of_employment_questions_form': freedom_of_employment_questions_form})


@login_required(login_url='login')
def edit(request, pk):
    try:
        freedom_of_employment_questions = get_object_or_404(FreedomOfEmploymentQuestions, household=pk)
        request.session['household'] = pk  # TODO: temporary, remove when search functionality is implemented
        if request.method == "POST":
            income_from_state_formset = modelformset_factory(IncomeFromStateAndCommonPropertyResources,
                                                             form=IncomeFromStateAndCommonPropertyResourcesForm, extra=5)
            aggri_or_non_aggri_labour_service_formset = modelformset_factory(AgriculturalOrNonAgriculturalLabourServices,
                                                                             form=AgriculturalOrNonAgriculturalLabourServicesForm, extra=5)

            income_from_state_forms = income_from_state_formset(request.POST, prefix='income_from_state')
            aggri_or_non_aggri_labour_service_forms = aggri_or_non_aggri_labour_service_formset(request.POST,
                                                                                                prefix='aggri_or_non_aggri_labour_service')
            freedom_of_employment_questions_form = FreedomOfEmploymentQuestionsForm(request.POST, instance=freedom_of_employment_questions)

            income_from_state_form_saved = False
            aggri_or_non_aggri_labour_service_form_saved = False
            freedom_of_employment_questions_form_saved = False

            if income_from_state_forms.is_valid() and aggri_or_non_aggri_labour_service_forms.is_valid() and freedom_of_employment_questions_form.is_valid():
                income_from_state_form_saved = save_forms(request, income_from_state_forms)
                aggri_or_non_aggri_labour_service_form_saved = save_forms(request, aggri_or_non_aggri_labour_service_forms)
                freedom_of_employment_questions_form_saved = save_form_with_no_has_change(request, freedom_of_employment_questions_form)

            if income_from_state_form_saved and aggri_or_non_aggri_labour_service_form_saved and freedom_of_employment_questions_form_saved:
                messages.success(request, 'Data saved successfully')
            else:
                return render(request, 'page16.html',
                              {'income_from_state_formset': income_from_state_forms,
                               'aggri_or_non_aggri_labour_service_formset': aggri_or_non_aggri_labour_service_forms,
                               'freedom_of_employment_questions_form': freedom_of_employment_questions_form})

        income_from_state_model_formset = modelformset_factory(IncomeFromStateAndCommonPropertyResources,
                                                               form=IncomeFromStateAndCommonPropertyResourcesForm, extra=5)
        income_from_state_result_set = IncomeFromStateAndCommonPropertyResources.objects.filter(household=pk)
        income_from_state_formset = income_from_state_model_formset(queryset=income_from_state_result_set,
                                                                    prefix='income_from_state')

        aggri_or_non_aggri_labour_service_model_formset = modelformset_factory(AgriculturalOrNonAgriculturalLabourServices,
                                                                               form=AgriculturalOrNonAgriculturalLabourServicesForm,
                                                                               extra=5)
        aggri_or_non_aggri_labour_service_result_set = AgriculturalOrNonAgriculturalLabourServices.objects.filter(household=pk)
        aggri_or_non_aggri_labour_service_formset = aggri_or_non_aggri_labour_service_model_formset(
            queryset=aggri_or_non_aggri_labour_service_result_set,
            prefix='aggri_or_non_aggri_labour_service')

        freedom_of_employment_questions_form = FreedomOfEmploymentQuestionsForm(instance=freedom_of_employment_questions)

        return render(request, 'page16.html', {'income_from_state_formset': income_from_state_formset,
                                               'aggri_or_non_aggri_labour_service_formset': aggri_or_non_aggri_labour_service_formset,
                                               'freedom_of_employment_questions_form': freedom_of_employment_questions_form})

    except Exception:
        return new(request)
