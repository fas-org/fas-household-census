from ..forms.ownership_section3 import CurrentOwnershipHoldingForm, HomesteadAreaForm
from ..models.ownership_section3 import CurrentOwnershipHolding, HomesteadArea
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
        holding_result_set = CurrentOwnershipHolding.objects.filter(household=request.session.get('household'))
        homestead_area_result_set = HomesteadArea.objects.filter(household=request.session.get('household'))
        if len(holding_result_set) == 0 and len(homestead_area_result_set) == 0:
            return new(request)
        return edit(request, request.session['household'])


@login_required(login_url='login')
def new(request):
    current_ownership_formset = formset_factory(CurrentOwnershipHoldingForm, formset=BaseFormSet, extra=5)
    homestead_area_formset = formset_factory(HomesteadAreaForm, formset=BaseFormSet, extra=1)
    if request.method == "POST":
        ownership_forms = current_ownership_formset(request.POST, prefix='owner')
        homestead_area_forms = homestead_area_formset(request.POST, prefix='homestead')
        form_saved = False
        if ownership_forms.is_valid() and homestead_area_forms.is_valid():
            for ownership_form in ownership_forms:
                if ownership_form.is_valid() and ownership_form.has_changed():
                    ownership = ownership_form.save(commit=False)
                    ownership.household = household.get(request.session['household'])
                    ownership.save()
                    form_saved = True  # TODO: add proper check to verify if all forms are saved

            for homestead_form in homestead_area_forms:
                if homestead_form.is_valid() and homestead_form.has_changed():
                    homestead = homestead_form.save(commit=False)
                    homestead.household = household.get(request.session['household'])
                    homestead.save()
                    form_saved = True

        if form_saved:
            messages.success(request, 'Data saved successfully')
            return redirect('ownership_edit', pk=request.session['household'])

    return render(request, 'ownership_section3.html', {'current_ownership_formset': current_ownership_formset(prefix='owner'),
                                                       'homesteadformset': homestead_area_formset(prefix='homestead')})


@login_required(login_url='login')
def edit(request, pk):
    try:
        request.session['household'] = pk  # TODO: temporary, remove when search functionality is implemented
        if request.method == "POST":
            current_ownership_formset = formset_factory(CurrentOwnershipHoldingForm, formset=BaseFormSet, extra=5)
            homestead_area_formset = formset_factory(HomesteadAreaForm, formset=BaseFormSet, extra=1)

            ownership_forms = current_ownership_formset(request.POST, prefix='owner')
            homestead_area_forms = homestead_area_formset(request.POST, prefix='homestead')

            # TODO: everytime creating new rows. we need to update them right?
            # TODO: do we need to add validation for duplicate rows as well? verify with user
            form_saved = False
            if ownership_forms.is_valid() and homestead_area_forms.is_valid():
                CurrentOwnershipHolding.objects.filter(household=pk).delete()
                HomesteadArea.objects.filter(household=pk).delete()
                for ownership_form in ownership_forms:
                    if ownership_form.is_valid() and ownership_form.has_changed():
                        ownership = ownership_form.save(commit=False)
                        ownership.household = household.get(request.session['household'])
                        ownership.save()
                        form_saved = True  # TODO: add proper check to verify if all forms are saved

                for homestead_form in homestead_area_forms:
                    if homestead_form.is_valid() and homestead_form.has_changed():
                        homestead = homestead_form.save(commit=False)
                        homestead.household = household.get(request.session['household'])
                        homestead.save()
                        form_saved = True

            if form_saved:
                messages.success(request, 'Data saved successfully')
            else:
                return render(request, 'ownership_section3.html',
                              {'current_ownership_formset': ownership_forms,
                               'homesteadformset': homestead_area_forms})

        current_ownership_model_formset = modelformset_factory(CurrentOwnershipHolding, form=CurrentOwnershipHoldingForm, extra=5)
        result_set = CurrentOwnershipHolding.objects.filter(household=pk)
        current_ownership_formset = current_ownership_model_formset(queryset=result_set, prefix='owner')

        homestead_area_model_formset = modelformset_factory(HomesteadArea, form=HomesteadAreaForm, extra=1)
        homestead_area_result_set = HomesteadArea.objects.filter(household=pk)
        homestead_area_formset = homestead_area_model_formset(queryset=homestead_area_result_set, prefix='homestead')

        return render(request, 'ownership_section3.html', {'current_ownership_formset': current_ownership_formset,
                                                           'homesteadformset': homestead_area_formset})

    except Exception:
        return new(request)


def get(household):
    try:
        homestead_area = HomesteadArea.objects.get(household=household)
    except HomesteadArea.DoesNotExist:
        homestead_area = None
    return homestead_area
