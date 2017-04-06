from ..forms.land_sales_forms_section4 import LandSoldForm, LandPurchasedForm
from ..models.land_sales_models_section4 import LandSold, LandPurchased
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
        landsoldform = LandSoldForm(request.POST)
        landpurchasedform = LandPurchasedForm(request.POST)

        if landsoldform.is_valid():
            landsold = landsoldform.save(commit=False)
            landsold.household = household.get(request.session['household'])
            landsold.save()

            landpurchased = landpurchasedform.save(commit=False)
            landpurchased.household = household.get(
                request.session['household'])
            landpurchased.save()
            messages.success(request, 'Data saved successfully')

            return redirect('landsales_edit',
                            household=request.session['household'])
    else:
        landsoldform = LandSoldForm()
        landpurchasedform = LandPurchasedForm()
    return render(request, 'land_sales_section4.html',
                  {'landsold_form': landsoldform,
                   'landpurchased_form': landpurchasedform})


@login_required(login_url='login')
def edit(request, pk):
    try:
        landsold = get_object_or_404(LandSold, household=pk)
        landpurchased = get_object_or_404(LandPurchased, household=pk)

        if request.method == "POST":
            landsoldform = LandSoldForm(request.POST, instance=landsold)
            landpurchasedform = LandPurchasedForm(request.POST,
                                                  instance=landpurchased)

            if landsoldform.is_valid() and landpurchasedform.is_valid():
                landsold = landsoldform.save(commit=False)
                landsold.save()

                landsold = landpurchasedform.save(commit=False)
                landsold.save()
                messages.success(request, 'Data saved successfully')

                return redirect('landsales_edit', pk=pk)
        else:
            landsoldform = LandSoldForm(instance=landsold)
            landpurchasedform = LandPurchasedForm(instance=landpurchased)
        return render(request, 'land_sales_section4.html',
                      {'landsold_form': landsoldform,
                       'landpurchased_form': landpurchasedform})
    except Exception:
        return new(request)


@login_required(login_url='login')
def get(household):
    try:
        landsold = LandSold.objects.get(household=household)
        landpurchased = LandPurchased.objects.get(household=household)
    except LandSold.DoesNotExist and LandPurchased.DoesNotExist:
        landsold = None
        landpurchased = None
    return landsold, landpurchased
