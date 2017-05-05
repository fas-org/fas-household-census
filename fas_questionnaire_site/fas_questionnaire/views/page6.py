from fas_questionnaire.views.common import save_formset, get_search_form
from ..forms.page6 import *
from ..models.page6 import *
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.forms.formsets import formset_factory, BaseFormSet
from django.contrib import messages
from django.forms import modelformset_factory


@login_required(login_url='login')
def init(request):
    if request.session.get('household') is None:
        return redirect('household_init')
    else:
        return edit(request, request.session['household'])


@login_required(login_url='login')
def edit(request, pk):
    request.session['household'] = pk
    if request.method == 'POST':
        # production_formset=formset_factory()
        production_formset = formset_factory(ProductionForm, formset=BaseFormSet, extra=5)
        production_forms = production_formset(request.POST, prefix='production',auto_id=False)

        sales_formset = formset_factory(SalesOfCropProducedForm, formset=BaseFormSet, extra=5)
        sales_forms = sales_formset(request.POST, prefix='sales',auto_id=False)

        if save_formset(production_forms, Production, pk) and save_formset(sales_forms, SalesOfProduction, pk):
            messages.success(request, 'Data saved successfully')
        return redirect('page6_edit', pk)

    production_model_formset = modelformset_factory(Production, form=ProductionForm, extra=5)
    result_set = Production.objects.filter(household=pk)
    production_formset = production_model_formset(queryset=result_set, prefix='production')

    Sales_model_formset = modelformset_factory(SalesOfProduction, form=SalesOfCropProducedForm, extra=5)
    result_set = SalesOfProduction.objects.filter(household=pk)
    sales_formset = Sales_model_formset(queryset=result_set, prefix='sales')

    return render(request, 'page6.html',
                  {'production_formset': production_formset,
                   'sales_formset': sales_formset,
                   'search_form': get_search_form()})
