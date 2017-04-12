from ..forms.production_and_sales_on_operational_holding_section6 import CroppingPatternAndCropScheduleForm, \
    CroppingPatternAndCropScheduleCommentsForm, ProductionAndSalesForm
from ..models.production_and_sales_on_operational_holding_section6 import CroppingPatternAndCropSchedule, \
    CroppingPatternAndCropScheduleComments, ProductionAndSales
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
        croppingPattern_result_set=CroppingPatternAndCropSchedule.objects.filter(household=request.session.get('household'))
        productionAndSales_result_set=ProductionAndSales.objects.filter(household=request.session.get('household'))
        if len(croppingPattern_result_set) == 0 and len(productionAndSales_result_set) == 0:
           return new(request)
        return edit(request, request.session['household'])


@login_required(login_url='login')
def new(request):
    croppingPattern_formset = formset_factory(CroppingPatternAndCropScheduleForm, formset=BaseFormSet, extra=5)
    productionAndSales_formset = formset_factory(ProductionAndSalesForm, formset=BaseFormSet, extra=5)
    croppingPatternCommentsForm = CroppingPatternAndCropScheduleCommentsForm()

    if request.method == "POST":
        croppingPatternForms = croppingPattern_formset(request.POST)
        croppingPatternCommentsForm = CroppingPatternAndCropScheduleCommentsForm(request.POST)
        productionAndSalesForms = productionAndSales_formset(request.POST)

        pattern_save = False
        sales_save = False
        if croppingPatternForms.is_valid() and croppingPatternCommentsForm.is_valid():
            for croppingPatternForm in croppingPatternForms:
                if croppingPatternForm.is_valid() and croppingPatternForm.has_changed():
                    croppingPattern = croppingPatternForm.save(commit=False)
                    croppingPattern.household = household.get(request.session['household'])
                    croppingPattern.save()
                    pattern_save = True

            croppingPatternComments = croppingPatternCommentsForm.save(commit=False)
            croppingPatternComments.household = household.get(request.session['household'])
            croppingPatternComments.save()
            pattern_save = True

        elif productionAndSalesForms.is_valid():
            for productionAndSalesForm in productionAndSalesForms:
                if productionAndSalesForm.is_valid() and productionAndSalesForm.has_changed():
                    productionAndSales = productionAndSalesForm.save(commit=False)
                    productionAndSales.household = household.get(request.session['household'])
                    productionAndSales.save()
                    sales_save = True

            if pattern_save or sales_save:
                messages.success(request, 'Data saved successfully')
            return redirect('production_and_sales_on_operational_holding_edit', pk=request.session['household'])
    # else:
    #     croppingPatternForms = CroppingPatternAndCropScheduleForm()
    #     croppingPatternCommentsForm = CroppingPatternAndCropScheduleCommentsForm()
    #     productionAndSalesForms = ProductionAndSalesForm()

    return render(request, 'production_and_sales_on_operational_holding_section6.html',
                  {'production_and_sales_on_operational_holding_formset': croppingPattern_formset,
                   'production_and_sales_on_operational_holding_comment_form': croppingPatternCommentsForm,
                   'production_and_sales_formset': productionAndSales_formset})


@login_required(login_url='login')
def edit(request, pk):
    try:
        request.session['household'] = pk  # TODO: temporary, remove when search functionality is implemented
        croppingPatternComments = get_object_or_404(CroppingPatternAndCropScheduleComments, household=pk)

        if request.method == "POST":
            croppingPattern_formset = formset_factory(CroppingPatternAndCropScheduleForm, formset=BaseFormSet, extra=5)
            productionAndSales_formset = formset_factory(ProductionAndSalesForm, formset=BaseFormSet, extra=5)

            croppingPatternForms = croppingPattern_formset(request.POST, instance=croppingPattern)
            croppingPatternCommentForm = CroppingPatternAndCropScheduleCommentsForm(request.POST,
                                                                                    instance=croppingPatternComments)
            productionAndSalesForms = productionAndSales_formset(request.POST, isinstance=productionAndSales)

            CroppingPatternAndCropSchedule.objects.filter(household=pk).delete()
            ProductionAndSales.objects.filter(household=pk).delete()

            pattern_save = False
            sales_save = False
            if croppingPatternForms.is_valid() and croppingPatternCommentForm.is_valid():
                for croppingPatternForm in croppingPatternForms:
                    if croppingPatternForm.is_valid() and croppingPatternForm.has_changed():
                        croppingPattern = croppingPatternForm.save(commit=False)
                        croppingPattern.household = household.get(request.session['household'])
                        croppingPattern.save()
                        pattern_save = True

                croppingPatternComments = croppingPatternCommentForm.save(commit=False)
                croppingPatternComments.household = household.get(request.session['household'])
                croppingPatternComments.save()
                pattern_save = True

            elif productionAndSalesForms.is_valid():
                for productionAndSalesForm in productionAndSalesForms:
                    if productionAndSalesForm.is_valid() and productionAndSalesForm.has_changed():
                        productionAndSales = productionAndSalesForm.save(commit=False)
                        productionAndSales.household = household.get(request.session['household'])
                        productionAndSales.save()
                        sales_save = True

            if pattern_save or sales_save:
                messages.success(request, 'Data saved successfully')
                return redirect('production_and_sales_on_operational_holding_edit', pk=pk)

        croppingPattern_model_formset=modelformset_factory(CroppingPatternAndCropSchedule,form=CroppingPatternAndCropScheduleForm,extra=5)
        croppingPattern_result_set=CroppingPatternAndCropSchedule.objects.filter(household=pk)
        croppingPatternset=croppingPattern_model_formset(queryset=croppingPattern_result_set)

        productionAndSales_model_form=modelformset_factory(ProductionAndSales,form=ProductionAndSalesForm,extr=5)
        productionAndSales_result_set=ProductionAndSales.objects.filter(household=pk)
        productionAndSalesset=productionAndSales_model_form(queryset=productionAndSales_result_set)

        croppingPatternCommentForms=CroppingPatternAndCropScheduleComments(instace=croppingPatternComments)

        return render(request, 'production_and_sales_on_operational_holding_section6.html',
                      {'production_and_sales_on_operational_holding_formset': croppingPatternset,
                       'production_and_sales_on_operational_holding_comment_form': croppingPatternCommentForms,
                       'production_and_sales_formset': productionAndSalesset})
    except Exception:
        return new(request)


def get(household):
    try:
        croppingPattern = CroppingPatternAndCropSchedule.objects.get(household=household)
        croppingPatternComments = CroppingPatternAndCropScheduleComments.objects.get(household=household)
        productionAndSales = ProductionAndSales.objects.get(household=household)

    except CroppingPatternAndCropSchedule.DoesNotExist:
        croppingPattern = None
        croppingPatternComments = None
        productionAndSales = None
    return croppingPattern, croppingPatternComments, productionAndSales
