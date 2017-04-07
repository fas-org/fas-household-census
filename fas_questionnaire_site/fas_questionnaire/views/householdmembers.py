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
        return edit(request, request.session['household'])


@login_required(login_url='login')
def new(request):
    class RequiredFormSet(BaseFormSet):
        def __init__(self, *args, **kwargs):
            super(RequiredFormSet, self).__init__(*args, **kwargs)
            for form in self.forms:
                form.empty_permitted = False

    householdMembersFormSet = formset_factory(HouseholdMembersForm, formset=BaseFormSet, extra=2)
    if request.method == "POST":
        forms = householdMembersFormSet(request.POST)

        if forms.is_valid():
            for form in forms:
                if form.is_valid():
                    member = form.save(commit=False)
                    member.household = Household.get(request.session['household'])
                    member.save()
            return redirect('householdmembers_edit', pk= request.session['household'])

    return render(request, 'householdmembers.html', { 'formset': householdMembersFormSet})


@login_required(login_url='login')
def edit(request, pk):
    householdMembersFormSet = modelformset_factory(HouseholdMembers,form=HouseholdMembersForm)
    result_set = HouseholdMembers.objects.filter(household=pk)
    formset = householdMembersFormSet(queryset=result_set)
    return render(request, 'householdmembers.html', { 'formset': formset})

@login_required(login_url='login')
def save(request):
    if request.method == "POST":
        posted_forms = request.POST.getlist('forms[]')
        for posted_form in posted_forms:
            form_data = json.loads(posted_form)
            form = HouseholdMembersForm(form_data)
            if form.is_valid():
                household_members = form.save(commit=False)
                household_members.household = Household.get(request.session['household'])
                household_members.save()
        messages.success(request, "Records saved successfully")
        return redirect('householdmembers_edit', pk= request.session['household'])
