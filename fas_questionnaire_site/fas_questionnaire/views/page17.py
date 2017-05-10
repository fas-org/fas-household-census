from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms.formsets import formset_factory, BaseFormSet
from django.forms import modelformset_factory
from ..forms.page17 import *
from ..models.page17 import *
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
        income_salary_formset = formset_factory(IncomeFromSalariesForm, formset=BaseFormSet, extra=1)
        income_business_formset = formset_factory(IncomeFromOtherBusinessActivitiesForm, formset=BaseFormSet, extra=1)
        animal_inventory_formset = formset_factory(AnimalResoursesInventoryForm, formset=BaseFormSet, extra=1)
        animal_feed_formset = formset_factory(AnimalResourcesFeedForm, formset=BaseFormSet, extra=1)
        other_expenditure_formset = formset_factory(OtherExpendituresForm, formset=BaseFormSet, extra=1)
        output_and_income_formset = formset_factory(OutputAndIncomeForm, formset=BaseFormSet, extra=1)

        income_salary_forms = income_salary_formset(request.POST, prefix='salary')
        income_business_forms = income_business_formset(request.POST, prefix='business')
        animal_inventory_forms = animal_inventory_formset(request.POST, prefix='inventory')
        animal_feed_forms = animal_feed_formset(request.POST, prefix='feed')
        other_expenditure_form = other_expenditure_formset(request.POST, prefix='other expenditure')
        output_and_income_form = output_and_income_formset(request.POST, prefix='output')

        if save_formset(income_salary_forms, IncomeFromSalaries, pk) \
                and save_formset(income_business_forms, IncomeFromOtherBusinessActivities, pk) \
                and save_formset(animal_inventory_forms, AnimalResoursesInventory, pk)\
                and save_formset(animal_feed_forms, AnimalResourcesFeed, pk)\
                and save_formset(other_expenditure_form, OtherExpenditure, pk)\
                and save_formset(output_and_income_form, OutputAndIncome, pk)\
                and save_formset(get_comments_formset_to_save(request), Comments, pk, 17):
            messages.success(request, 'Data saved successfully')
        return redirect('page17_edit', pk)

    income_salary_model_formset = modelformset_factory(IncomeFromSalaries, form=IncomeFromSalariesForm, extra=1,widgets = get_household_members_as_widget(pk, 'worker_name'))
    income_salary_result_set = IncomeFromSalaries.objects.filter(household=pk)
    income_salary_formset = income_salary_model_formset(queryset=income_salary_result_set, prefix='salary')

    income_business_model_formset = modelformset_factory(IncomeFromOtherBusinessActivities,
                                                         form=IncomeFromOtherBusinessActivitiesForm, extra=1, widgets = get_household_members_as_widget(pk, 'name_of_worker'))
    income_business_result_set = IncomeFromOtherBusinessActivities.objects.filter(household=pk)
    income_business_formset = income_business_model_formset(queryset=income_business_result_set, prefix='business')

    animal_inventory_model_formset = modelformset_factory(AnimalResoursesInventory, form=AnimalResoursesInventoryForm,
                                                          extra=1)
    animal_inventory_result_set = AnimalResoursesInventory.objects.filter(household=pk)
    animal_inventory_formset = animal_inventory_model_formset(queryset=animal_inventory_result_set, prefix='inventory')

    animal_feed_model_formset = modelformset_factory(AnimalResourcesFeed, form=AnimalResourcesFeedForm, extra=1)
    animal_feed_result_set = AnimalResourcesFeed.objects.filter(household=pk)
    animal_feed_formset = animal_feed_model_formset(queryset=animal_feed_result_set, prefix='feed')

    other_expenditure_model_formset = modelformset_factory(OtherExpenditure, form=OtherExpendituresForm, extra=1)
    other_expenditure_result_set = OtherExpenditure.objects.filter(household=pk)
    other_expenditure_formset = other_expenditure_model_formset(queryset=other_expenditure_result_set,
                                                                prefix='other expenditure')

    output_and_income_model_formset = modelformset_factory(OutputAndIncome, form=OutputAndIncomeForm, extra=1)
    output_and_income_result_set = OutputAndIncome.objects.filter(household=pk)
    output_and_income_formset = output_and_income_model_formset(queryset=output_and_income_result_set, prefix='output')

    return render(request, 'page17.html', {'income_salary_formset': income_salary_formset,
                                           'income_business_formset': income_business_formset,
                                           'animal_inventory_formset': animal_inventory_formset,
                                           'animal_feed_formset': animal_feed_formset,
                                           'other_expenditure_formset': other_expenditure_formset,
                                           'output_and_income_formset': output_and_income_formset,
                                           'search_form': get_search_form(),
                                           'comments': get_comments_formset(pk, 17)})
