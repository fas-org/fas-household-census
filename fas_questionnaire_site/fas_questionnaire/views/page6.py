from fas_questionnaire.views.common import save_formset, get_search_form, get_crop_first_digit_as_widget, get_comments_formset_to_save, get_comments_formset
from ..forms.page6 import *
from ..models.page6 import *
from ..models.common import Comments
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
        production_formset = formset_factory(ProductionForm, formset=BaseFormSet, extra=1)
        production_forms = production_formset(request.POST, prefix='production',auto_id=False)

        sales_formset = formset_factory(SalesOfCropProducedForm, formset=BaseFormSet, extra=1)
        sales_forms = sales_formset(request.POST, prefix='sales',auto_id=False)

        if save_formset(production_forms, Production, pk) and save_formset(sales_forms, SalesOfProduction, pk) and save_formset(get_comments_formset_to_save(request), Comments, pk, 6):
            messages.success(request, 'Data saved successfully')
        return redirect('page6_edit', pk)

    crop_digits_list = get_crop_first_digit_as_widget(pk,'crop_number_first_digit').copy()
    crop_digits_list.update(get_crop_first_digit_as_widget(pk,'crop_number_second_digit'))
    production_model_formset = modelformset_factory(Production, form=ProductionForm, extra=1,widgets=crop_digits_list)
    result_set = Production.objects.filter(household=pk)
    production_formset = production_model_formset(queryset=result_set, prefix='production')

    Sales_model_formset = modelformset_factory(SalesOfProduction, form=SalesOfCropProducedForm, extra=1)
    result_set = SalesOfProduction.objects.filter(household=pk)
    sales_formset = Sales_model_formset(queryset=result_set, prefix='sales')

    return render(request, 'page6.html',
                  {'production_formset': production_formset,
                   'sales_formset': sales_formset,
                   'search_form': get_search_form(),
                   'comments': get_comments_formset(pk, 6)})
