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
    if request.method=='POST':
        productionAndSales_formset=formset_factory(ProductionAndSalesForm,formset=BaseFormSet,extra=5)
        forms=productionAndSales_formset(request.POST,prefix='sales')

        if save_formset(forms,ProductionAndSales,pk):
            messages.success(request,'Data saved successfully')
        return redirect('page6_edit',pk)

    productionAndSales_model_formset=modelformset_factory(ProductionAndSales,form=ProductionAndSalesForm,extra=5)
    result_set=ProductionAndSales.objects.filter(household=pk)
    formset = productionAndSales_model_formset(queryset=result_set,prefix='sales')
    return render(request, 'page6.html',
                          {'production_and_sales_formset': formset,
                           'search_form': get_search_form()})
