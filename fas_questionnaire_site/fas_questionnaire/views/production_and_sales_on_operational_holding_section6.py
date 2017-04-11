from ..forms.production_and_sales_on_operational_holding_section6 import CropProductionOnOperationalHoldingForm, \
    CropProductionOnOperationalHoldingCommentsForm,ProductionAndSalesForm
from ..models.production_and_sales_on_operational_holding_section6 import CropProductionOnOperationalHolding, \
    CropProductionOnOperationalHoldingComments,ProductionAndSales
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
        cropProductionForm = CropProductionOnOperationalHoldingForm(request.POST)
        cropProductionCommentsForm = CropProductionOnOperationalHoldingCommentsForm(request.POST)
        productionAndSalesForm=ProductionAndSalesForm(request.POST)

        if cropProductionForm.is_valid()  and cropProductionCommentsForm.is_valid():
            cropProduction = cropProductionForm.save(commit=False)
            cropProduction.household = household.get(request.session['household'])
            cropProduction.save()

            cropProductionComments = cropProductionCommentsForm.save(commit=False)
            cropProductionComments.household = household.get(request.session['household'])
            cropProductionComments.save()
        elif  productionAndSalesForm.is_valid():
            productionAndSales=productionAndSalesForm.save(commit=False)
            productionAndSales.household=household.get(request.session['household'])
            productionAndSales.save()

            messages.success(request, 'Data saved successfully')
            return redirect('production_and_sales_on_operational_holding_edit', pk=request.session['household'])
    else:
        cropProductionForm = CropProductionOnOperationalHoldingForm()
        cropProductionCommentsForm = CropProductionOnOperationalHoldingCommentsForm()
        productionAndSalesForm= ProductionAndSalesForm()

    return render(request, 'production_and_sales_on_operational_holding_section6.html',
                  {'production_and_sales_on_operational_holding_form': cropProductionForm,
                   'production_and_sales_on_operational_holding_comment_form': cropProductionCommentsForm,
                   'production_and_sales_form': productionAndSalesForm})


@login_required(login_url='login')
def edit(request, pk):
    try:
        request.session['household'] = pk  # TODO: temporary, remove when search functionality is implemented
        cropProduction = get_object_or_404(CropProductionOnOperationalHolding, household=pk)
        cropProductionComments = get_object_or_404(CropProductionOnOperationalHoldingComments, household=pk)
        productionAndSales=get_object_or_404(ProductionAndSales,household=pk)
        if request.method == "POST":
            form = CropProductionOnOperationalHoldingForm(request.POST, instance=cropProduction)
            commentForm = CropProductionOnOperationalHoldingCommentsForm(request.POST, instance=cropProductionComments)
            productionAndSalesForm=ProductionAndSalesForm(request.POST,isinstance=productionAndSales)

            if form.is_valid() and commentForm.is_valid():
                cropProduction = form.save(commit=False)
                cropProduction.save()

                cropProductionComments = commentForm.save(commit=False)
                cropProductionComments.save()
            elif productionAndSalesForm.is_valid():
                productionAndSales=productionAndSalesForm.save(commit=False)
                productionAndSales.save()

                messages.success(request, 'Data saved successfully')

                return redirect('production_and_sales_on_operational_holding_edit', pk=pk)
        else:
            form = CropProductionOnOperationalHoldingForm(instance=cropProduction)
            commentForm = CropProductionOnOperationalHoldingCommentsForm(instance=cropProductionComments)
            productionAndSalesForm=ProductionAndSalesForm(instance=productionAndSales)
        return render(request, 'production_and_sales_on_operational_holding_section6.html',
                      {'production_and_sales_on_operational_holding_form': form,
                       'production_and_sales_on_operational_holding_comment_form':commentForm,
                       'production_and_sales_form':productionAndSalesForm})
    except Exception:
        return new(request)


def get(household):
    try:
        cropProduction = CropProductionOnOperationalHolding.objects.get(household=household)
        cropProductionComments = CropProductionOnOperationalHoldingComments.objects.get(household=household)
        productionAndSales = ProductionAndSales.objects.get(household=household)

    except CropProductionOnOperationalHolding.DoesNotExist:
        cropProduction = None
        cropProductionComments = None
        productionAndSales = None
    return cropProduction, cropProductionComments,productionAndSales
