from ..forms.introduction_forms_section1 import HouseholdIntroductionForm
from ..models.introduction_models_section1 import HouseholdIntroduction
from django.shortcuts import get_object_or_404, render, redirect
from . import household as household
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.forms.formsets import formset_factory, BaseFormSet
from django.forms import modelformset_factory
from ..models.household_models import Household
from ..forms.householdmembers import HouseholdMembersForm
from ..models.householdmembers import HouseholdMembers



@login_required(login_url='login')
def init(request):
    if request.session.get('household') is None:
        return new(request)
    else:
        return edit(request, request.session['household'])


@login_required(login_url='login')
def new(request):
    household_members_formset = formset_factory(HouseholdMembersForm, formset=BaseFormSet, extra=5)

    if request.method == "POST":
        introduction_form = HouseholdIntroductionForm(request.POST)
        household_forms = household_members_formset(request.POST)
        if introduction_form.is_valid() and household_forms.is_valid():
            introduction = introduction_form.save(commit=False)
            introduction.household = household.get(request.session['household'])
            introduction.save()

            for household_form in household_forms:
                if household_form.is_valid() and household_form.has_changed():
                    member = household_form.save(commit=False)
                    member.household = Household.objects.get(pk=request.session['household'])
                    member.save()

            messages.success(request, 'Data saved successfully')
            return redirect('introduction_edit', pk=request.session['household'])
    else:
        introduction_form = HouseholdIntroductionForm()

    return render(request, 'page1.html', {'introduction_form': introduction_form,'household_formset': household_members_formset})

@login_required(login_url='login')
def edit(request, pk):
    try:
        request.session['household'] = pk  # TODO: temporary, remove when search functionality is implemented
        introduction = get_object_or_404(HouseholdIntroduction, household=pk)
        introduction_form = HouseholdIntroductionForm(instance=introduction)
        household_members_formset = formset_factory(HouseholdMembersForm, formset=BaseFormSet, extra=5)
        if request.method == "POST":

            introduction_form = HouseholdIntroductionForm(request.POST, instance=introduction)
            household_members_forms = household_members_formset(request.POST)

            HouseholdMembers.objects.filter(household=pk).delete()

            if household_members_forms.is_valid():
                for household_members_form in household_members_forms:
                    if household_members_form.is_valid() and household_members_form.has_changed():
                        member = household_members_form.save(commit=False)
                        member.household = Household.objects.get(pk=request.session['household'])
                        member.save()
            if introduction_form.is_valid():
                introduction = introduction_form.save(commit=False)
                introduction.save()
                messages.success(request, 'Data saved successfully')
            return redirect('introduction_edit', pk=pk)

        household_members_model_formset = modelformset_factory(HouseholdMembers, form=HouseholdMembersForm, extra=5)
        result_set = HouseholdMembers.objects.filter(household=pk)
        household_members_formset = household_members_model_formset(queryset=result_set)

        return render(request, 'page1.html', {'introduction_form': introduction_form, 'household_formset': household_members_formset})
    except Exception:
        return new(request)

def get(household):
    try:
        introduction = HouseholdIntroduction.objects.get(household=household)
    except HouseholdIntroduction.DoesNotExist:
        introduction = None
    return introduction
