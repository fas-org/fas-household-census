from ..forms import HouseholdForm
from ..models import Household
from django.shortcuts import get_object_or_404, render, redirect


def new(request):
    if request.method == "POST":
        form = HouseholdForm(request.POST)
        if form.is_valid():
            household = form.save(commit=False)
            household.save()
            request.session['household'] = household.pk
            return redirect('household_edit', pk=household.pk)
    else:
        form = HouseholdForm()
    return render(request, 'household_section1.html', {'household_form': form})


def edit(request, pk):
    household = get_object_or_404(Household, pk=pk)
    if request.method == "POST":
        form = HouseholdForm(request.POST, instance=household)
        if form.is_valid():
            household = form.save(commit=False)
            household.save()
            return redirect('household_edit', pk=pk)
    else:
        form = HouseholdForm(instance=household)
    return render(request, 'household_section1.html', {'household_form': form})


def get(pk):
    try:
        household = Household.objects.get(pk=pk)
    except Household.DoesNotExist:
        household = None
    return household
