from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.forms.formsets import formset_factory, BaseFormSet
from django.forms import modelformset_factory
import json
from ..forms.householdmembers import HouseholdMembersForm
from ..models.householdmembers import HouseholdMembers
from ..models.household_models import Household


@login_required(login_url='login')
def init(request):
    if request.session.get('household') is None:
        return new(request)
    else:
        result_set = HouseholdMembers.objects.filter(household=request.session.get('household'))
        if len(result_set) == 0:
            return new(request)
        return edit(request, request.session['household'])


@login_required(login_url='login')
def new(request):
    household_members_formset = formset_factory(HouseholdMembersForm, formset=BaseFormSet, extra=5)
    if request.method == "POST":
        forms = household_members_formset(request.POST)

        if forms.is_valid():
            for form in forms:
                if form.is_valid() and form.has_changed():
                    member = form.save(commit=False)
                    member.household = Household.objects.get(pk=request.session['household'])
                    member.save()
            return redirect('householdmembers_edit', pk= request.session['household'])

    return render(request, 'householdmembers.html', { 'formset': household_members_formset})


@login_required(login_url='login')
def edit(request, pk):
    if request.method == "POST":
        household_members_formset = formset_factory(HouseholdMembersForm, formset=BaseFormSet, extra=5)
        forms = household_members_formset(request.POST)
        HouseholdMembers.objects.filter(household=pk).delete()

        if forms.is_valid():
            for form in forms:
                if form.is_valid() and form.has_changed():
                    member = form.save(commit=False)
                    member.household = Household.objects.get(pk=request.session['household'])
                    member.save()

    household_members_model_formset = modelformset_factory(HouseholdMembers,form=HouseholdMembersForm, extra=5)
    result_set = HouseholdMembers.objects.filter(household=pk)
    formset = household_members_model_formset(queryset=result_set)
    return render(request, 'householdmembers.html', { 'formset': formset})
