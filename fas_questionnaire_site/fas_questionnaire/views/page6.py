from ..forms.page6 import *
from ..models.page6 import *
from django.shortcuts import get_object_or_404, render, redirect
from . import household as household
from django.contrib.auth.decorators import login_required
from django.forms.formsets import formset_factory, BaseFormSet
from django.contrib import messages
from django.forms import modelformset_factory


@login_required(login_url='login')
def init(request):
    if request.session.get('household') is None:
        return new(request)
    else:
        productionAndSales_result_set=ProductionAndSales.objects.filter(household=request.session.get('household'))
        if len(productionAndSales_result_set) == 0:
           return new(request)
        return edit(request, request.session['household'])


@login_required(login_url='login')
def new(request):
    productionAndSales_formset = formset_factory(ProductionAndSalesForm, formset=BaseFormSet, extra=5)

    if request.method == "POST":
        productionAndSalesForms = productionAndSales_formset(request.POST)

        sales_save = False
        if productionAndSalesForms.is_valid():
            for productionAndSalesForm in productionAndSalesForms:
                if productionAndSalesForm.is_valid() and productionAndSalesForm.has_changed():
                    productionAndSales = productionAndSalesForm.save(commit=False)
                    productionAndSales.household = household.get(request.session['household'])
                    productionAndSales.save()
                    sales_save = True

            if sales_save:
                messages.success(request, 'Data saved successfully')
            return redirect('page6_edit', pk=request.session['household'])

    return render(request, 'page6.html',
                  {'production_and_sales_formset': productionAndSales_formset})


@login_required(login_url='login')
def edit(request, pk):
    try:
        request.session['household'] = pk  # TODO: temporary, remove when search functionality is implemented

        if request.method == "POST":
            productionAndSales_formset = formset_factory(ProductionAndSalesForm, formset=BaseFormSet, extra=5)
            productionAndSalesForms = productionAndSales_formset(request.POST)

            sales_save = False
            if productionAndSalesForms.is_valid():
                ProductionAndSales.objects.filter(household=pk).delete()
                for productionAndSalesForm in productionAndSalesForms:
                    if productionAndSalesForm.is_valid() and productionAndSalesForm.has_changed():
                        productionAndSales = productionAndSalesForm.save(commit=False)
                        productionAndSales.household = household.get(request.session['household'])
                        productionAndSales.save()
                        sales_save = True

            if sales_save:
                messages.success(request, 'Data saved successfully')

        productionAndSales_model_form=modelformset_factory(ProductionAndSales, form=ProductionAndSalesForm, extra=5)
        productionAndSales_result_set=ProductionAndSales.objects.filter(household=pk)
        productionAndSalesset=productionAndSales_model_form(queryset=productionAndSales_result_set)

        return render(request, 'page6.html',
                      {'production_and_sales_formset': productionAndSalesset})
    except Exception:
        return new(request)


def get(household):
    try:
        productionAndSales = ProductionAndSales.objects.get(household=household)

    except ProductionAndSales.DoesNotExist:
        productionAndSales = None
    return productionAndSales
