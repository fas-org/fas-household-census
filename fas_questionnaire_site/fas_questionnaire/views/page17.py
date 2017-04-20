from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms.formsets import formset_factory, BaseFormSet
from django.forms import modelformset_factory
from ..forms.page17 import *
from ..models.page17 import *
from .common import save_formset, save_forms


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
        income_salary_formset = formset_factory(IncomeFromSalariesForm, formset=BaseFormSet, extra=5)
        income_business_formset = formset_factory(IncomeFromOtherBusinessActivitiesForm, formset=BaseFormSet, extra=5)
        income_salary_forms = income_salary_formset(request.POST, prefix='salary')
        income_business_forms = income_business_formset(request.POST, prefix='business')
        if save_formset(income_salary_forms, IncomeFromSalaries, pk) and save_formset(income_business_forms,IncomeFromOtherBusinessActivities,pk):
            messages.success(request, 'Data saved succesfully')
        return redirect('page17_edit', pk)

    income_salary_model_formset = modelformset_factory(IncomeFromSalaries, form=IncomeFromSalariesForm, extra=5)
    income_salary_result_set = IncomeFromSalaries.objects.filter(household=pk)
    income_salary_formset = income_salary_model_formset(queryset=income_salary_result_set, prefix='salary')

    income_business_model_formset = modelformset_factory(IncomeFromOtherBusinessActivities,
                                                         form=IncomeFromOtherBusinessActivitiesForm, extra=5)
    income_business_result_set = IncomeFromOtherBusinessActivities.objects.filter(household=pk)
    income_business_formset = income_business_model_formset(queryset=income_business_result_set, prefix='business')

    return render(request, 'page17.html', {'income_salary_formset': income_salary_formset,
                                           'income_business_formset': income_business_formset})
