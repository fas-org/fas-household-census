from ..forms.page17 import *
from ..models.page17 import *
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
        income_result = IncomeFromSalaries.objects.filter(household=request.session.get('household'))
        if len(income_result) == 0:
            return new(request)
        return edit(request, request.session['household'])


@login_required(login_url='login')
def new(request):
    income_formset = formset_factory(IncomeFromSalariesForm, formset=BaseFormSet, extra=5)
    if request.method == "POST":
        income_forms = income_formset(request.POST, prefix='salary')
        income_form_saved = False
        if income_forms.is_valid():
            income_form_saved = save_forms(request, income_forms)

        if income_form_saved:
            messages.success(request, 'Data saved successfully')
            return redirect('page17_edit', pk=request.session['household'])
        else:
            return render(request, 'page17.html',
                          {'income_formset': income_forms,
                           })
    return render(request, 'page17.html', {'income_formset': income_formset(prefix='salary'),
                                           })


@login_required(login_url='login')
def edit(request, pk):
    try:
        request.session['household'] = pk  # TODO: temporary, remove when search functionality is implemented
        if request.method == "POST":
            income_formset = modelformset_factory(IncomeFromSalaries, form=IncomeFromSalariesForm, extra=5)

            income_forms = income_formset(request.POST, prefix='salary')

            income_form_saved = False

            if income_forms.is_valid():
                income_form_saved = save_forms(request, income_forms)

            if income_form_saved:
                messages.success(request, 'Data saved successfully')
            else:
                return render(request, 'page17.html',
                              {'income_formset': income_forms,
                               })

        income_model_formset = modelformset_factory(IncomeFromSalaries, form=IncomeFromSalariesForm, extra=5)
        income_result_set = IncomeFromSalaries.objects.filter(household=pk)
        income_formset = income_model_formset(queryset=income_result_set, prefix='salary')


        return render(request, 'page17.html', {'income_formset': income_formset,
                                               })
    except Exception:
        return new(request)
