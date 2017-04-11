from ..forms.production_and_sales_on_operational_holding_section6 import CroppingPatternAndCropScheduleForm, \
    CroppingPatternAndCropScheduleCommentsForm,ProductionAndSalesForm
from ..models.production_and_sales_on_operational_holding_section6 import CroppingPatternAndCropSchedule, \
    CroppingPatternAndCropScheduleComments,ProductionAndSales
from django.shortcuts import get_object_or_404, render, redirect
from . import household as household
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required(login_url='login')
def init(request):
    if request.session.get('household') is None:
        return new(request)
    else:
        return edit(request, request.session['household'])


@login_required(login_url='login')
def new(request):
    if request.method == "POST":
        croppingPatternForm = CroppingPatternAndCropScheduleForm(request.POST)
        croppingPatternCommentsForm = CroppingPatternAndCropScheduleCommentsForm(request.POST)
        productionAndSalesForm=ProductionAndSalesForm(request.POST)

        if croppingPatternForm.is_valid()  and croppingPatternCommentsForm.is_valid():
            croppingPattern = croppingPatternForm.save(commit=False)
            croppingPattern.household = household.get(request.session['household'])
            croppingPattern.save()

            croppingPatternComments = croppingPatternCommentsForm.save(commit=False)
            croppingPatternComments.household = household.get(request.session['household'])
            croppingPatternComments.save()
        elif  productionAndSalesForm.is_valid():
            productionAndSales=productionAndSalesForm.save(commit=False)
            productionAndSales.household=household.get(request.session['household'])
            productionAndSales.save()

            messages.success(request, 'Data saved successfully')
            return redirect('production_and_sales_on_operational_holding_edit', pk=request.session['household'])
    else:
        croppingPatternForm = CroppingPatternAndCropScheduleForm()
        croppingPatternCommentsForm = CroppingPatternAndCropScheduleCommentsForm()
        productionAndSalesForm= ProductionAndSalesForm()

    return render(request, 'production_and_sales_on_operational_holding_section6.html',
                  {'production_and_sales_on_operational_holding_form': croppingPatternForm,
                   'production_and_sales_on_operational_holding_comment_form': croppingPatternCommentsForm,
                   'production_and_sales_form': productionAndSalesForm})


@login_required(login_url='login')
def edit(request, pk):
    try:
        request.session['household'] = pk  # TODO: temporary, remove when search functionality is implemented
        croppingPattern = get_object_or_404(CroppingPatternAndCropSchedule, household=pk)
        croppingPatternComments = get_object_or_404(CroppingPatternAndCropScheduleComments, household=pk)
        productionAndSales=get_object_or_404(ProductionAndSales,household=pk)
        if request.method == "POST":
            croppingPatternForm = CroppingPatternAndCropScheduleForm(request.POST, instance=croppingPattern)
            croppingPatternCommentForm = CroppingPatternAndCropScheduleCommentsForm(request.POST, instance=croppingPatternComments)
            productionAndSalesForm=ProductionAndSalesForm(request.POST,isinstance=productionAndSales)

            if croppingPatternForm.is_valid() and croppingPatternCommentForm.is_valid():
                croppingPattern = croppingPatternForm.save(commit=False)
                croppingPattern.save()

                croppingPatternComments = croppingPatternCommentForm.save(commit=False)
                croppingPatternComments.save()
            elif productionAndSalesForm.is_valid():
                productionAndSales=productionAndSalesForm.save(commit=False)
                productionAndSales.save()

                messages.success(request, 'Data saved successfully')

                return redirect('production_and_sales_on_operational_holding_edit', pk=pk)
        else:
            croppingPatternForm = CroppingPatternAndCropScheduleForm(instance=croppingPattern)
            croppingPatternCommentForm = CroppingPatternAndCropScheduleCommentsForm(instance=croppingPatternComments)
            productionAndSalesForm=ProductionAndSalesForm(instance=productionAndSales)
        return render(request, 'production_and_sales_on_operational_holding_section6.html',
                      {'production_and_sales_on_operational_holding_form': croppingPatternForm,
                       'production_and_sales_on_operational_holding_comment_form':croppingPatternCommentForm,
                       'production_and_sales_form':productionAndSalesForm})
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
    return croppingPattern, croppingPatternComments,productionAndSales
