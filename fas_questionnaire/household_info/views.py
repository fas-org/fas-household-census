from django.shortcuts import render, get_object_or_404, redirect
from .models import Household, HouseholdMembers
from .forms import HouseholdForm, HouseholdMembersForm


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


def household_members_new(request):
    if request.method == "POST":
        form = HouseholdMembersForm(request.POST)
        if form.is_valid():
            householdmembers = form.save(commit=False)
            householdmembers.save()
            return redirect('household_members_edit', pk=householdmembers.pk)
    else:
        form = HouseholdMembersForm()
    return render(request, 'household_info/household_members_edit.html', {'form': form})


def household_members_edit(request, pk):
    householdmembers = get_object_or_404(HouseholdMembers, pk=pk)
    if request.method == "POST":
        form = HouseholdMembersForm(request.POST, instance=householdmembers)
        if form.is_valid():
            householdmembers = form.save(commit=False)
            householdmembers.save()
            return redirect('household_members_edit', pk=householdmembers.pk)
    else:
        form = HouseholdMembersForm(instance=householdmembers)
    return render(request, 'household_info/household_members_edit.html', {'form': form})
