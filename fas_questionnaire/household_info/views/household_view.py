from django.shortcuts import render, get_object_or_404, redirect
from ..models import Household
from ..forms import HouseholdForm


def household_new(request):
    if request.method == "POST":
        form = HouseholdForm(request.POST)
        if form.is_valid():
            household = form.save(commit=False)
            household.save()
            return redirect('household_edit', pk=household.pk)
    else:
        form = HouseholdForm()
    return render(request, 'household_info/household_edit.html', {'form': form})


def household_edit(request, pk):
    household = get_object_or_404(Household, pk=pk)
    if request.method == "POST":
        form = HouseholdForm(request.POST, instance=household)
        if form.is_valid():
            household = form.save(commit=False)
            household.save()
            return redirect('household_edit', pk=household.pk)
    else:
        form = HouseholdForm(instance=household)
    return render(request, 'household_info/household_edit.html', {'form': form})
