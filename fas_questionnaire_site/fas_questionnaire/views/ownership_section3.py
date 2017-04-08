from ..forms.ownership_section3 import CurrentOwnershipHoldingForm
from ..models.ownership_section3 import CurrentOwnershipHolding
from django.shortcuts import get_object_or_404, render, redirect
from . import household as household
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.forms.formsets import formset_factory, BaseFormSet
from django.forms import modelformset_factory


@login_required(login_url='login')
def init(request):
    if request.session.get('household') is None:
        return new(request)
    else:
        result_set = CurrentOwnershipHolding.objects.filter(household=request.session.get('household'))
        if len(result_set) == 0:
            return new(request)
        return edit(request, request.session['household'])


@login_required(login_url='login')
def new(request):
    current_ownership_formset = formset_factory(CurrentOwnershipHoldingForm, formset=BaseFormSet, extra=5)
    if request.method == "POST":
        forms = current_ownership_formset(request.POST)

        if forms.is_valid():
            for form in forms:
                if form.is_valid() and form.has_changed():
                    ownership = form.save(commit=False)
                    ownership.household = household.get(request.session['household'])
                    ownership.save()
                    form_saved = True  # TODO: add proper check to verify if all forms are saved
        if form_saved:
            messages.success(request, 'Data saved successfully')
            return redirect('ownership_edit', pk=request.session['household'])

    return render(request, 'ownership_section3.html', {'formset': current_ownership_formset})


@login_required(login_url='login')
def edit(request, pk):
    try:
        request.session['household'] = pk  # TODO: temporary, remove when search functionality is implemented
        if request.method == "POST":
            current_ownership_formset = formset_factory(CurrentOwnershipHoldingForm, formset=BaseFormSet, extra=5)
            forms = current_ownership_formset(request.POST)
            CurrentOwnershipHolding.objects.filter(household=pk).delete()
            # TODO: everytime creating new rows. we need to update them right?
            # TODO: do we need to add validation for duplicate rows as well? verify with user
            if forms.is_valid():
                for form in forms:
                    if form.is_valid() and form.has_changed():
                        ownership = form.save(commit=False)
                        ownership.save()
                        form_saved = True  # TODO: add proper check to verify if all forms are saved
            if form_saved:
                messages.success(request, 'Data saved successfully')

        current_ownership_model_formset = modelformset_factory(CurrentOwnershipHolding, form=CurrentOwnershipHoldingForm, extra=5)
        result_set = CurrentOwnershipHolding.objects.filter(household=pk)
        formset = current_ownership_model_formset(queryset=result_set)
        return render(request, 'ownership_section3.html', {'formset': formset})

    except Exception:
        return new(request)


def get(household):
    try:
        ownership = CurrentOwnershipHolding.objects.get(household=household)
    except CurrentOwnershipHolding.DoesNotExist:
        ownership = None
    return ownership
