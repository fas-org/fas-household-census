from ..forms.page4 import LandMortgagedInForm
from ..models.page4 import LandMortgagedIn
from ..forms.page4 import LandMortgagedOutForm
from ..models.page4 import LandMortgagedOut
from ..forms.page4 import LandLeasedInOnShareRentForm
from ..models.page4 import LandLeasedInOnShareRent
from ..forms.page4 import LandLeasedOutOnShareRentForm
from ..models.page4 import LandLeasedOutOnShareRent
from django.shortcuts import get_object_or_404, render, redirect
from . import household as household
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.forms.formsets import formset_factory, BaseFormSet
from django.forms import modelformset_factory
import pdb
from .common import *

@login_required(login_url='login')
def init(request):
    #pdb.set_trace()
    if request.session.get('household') is None:
        return new(request)
    else:
        result_set_LM_in = LandMortgagedIn.objects.filter(household_number=request.session.get('household'))
        result_set_LM_out = LandMortgagedOut.objects.filter(household_number=request.session.get('household'))
        result_set_lnd_lsd_in_shr_rent = LandLeasedInOnShareRent.objects.filter(household_number=request.session.get('household'))
        result_set_lnd_lsd_out_shr_rent = LandLeasedOutOnShareRent.objects.filter(household_number=request.session.get('household'))

        if  len(result_set_LM_in) == 0 and \
            len(result_set_LM_out) == 0 and \
            len(result_set_lnd_lsd_in_shr_rent) == 0 and \
            len(result_set_lnd_lsd_out_shr_rent) == 0:
            return new(request)
        return edit(request, request.session['household'])


@login_required(login_url='login')
def new(request):
    #pdb.set_trace()
    land_mortgage_in_formset = formset_factory(LandMortgagedInForm, formset=BaseFormSet, extra=5)
    land_mortgage_out_formset = formset_factory(LandMortgagedOutForm, formset=BaseFormSet, extra=5)
    lnd_lsd_in_shr_rent_formset = formset_factory(LandLeasedInOnShareRentForm, formset=BaseFormSet, extra=5)
    lnd_lsd_out_shr_rent_formset = formset_factory(LandLeasedOutOnShareRentForm, formset=BaseFormSet, extra=5)

    if request.method == "POST":
        land_mortgage_in_forms = land_mortgage_in_formset(request.POST, prefix='lm_in')
        land_mortgage_out_forms = land_mortgage_out_formset(request.POST, prefix='lm_out')
        lnd_lsd_in_shr_rent_forms = lnd_lsd_in_shr_rent_formset(request.POST, prefix='lnd_lsd_in_shr_rent')
        lnd_lsd_out_shr_rent_forms = lnd_lsd_out_shr_rent_formset(request.POST, prefix='lnd_lsd_out_shr_rent')


        form_land_mortgage_in_saved = False
        form_land_mortgage_out_saved = False
        form_lnd_lsd_in_shr_rent_saved = False
        form_lnd_lsd_out_shr_rent_saved = False

        if land_mortgage_in_forms.is_valid() and \
                land_mortgage_out_forms.is_valid() and \
                lnd_lsd_in_shr_rent_forms.is_valid() and \
                lnd_lsd_out_shr_rent_forms.is_valid():

            for land_mortgage_in_form in land_mortgage_in_forms:
                if land_mortgage_in_form.is_valid() and land_mortgage_in_form.has_changed():
                    land_mortgage_in = land_mortgage_in_form.save(commit=False)
                    land_mortgage_in.household_number = household.get(request.session['household'])
                    land_mortgage_in.save()
                    form_land_mortgage_in_saved = True

            for land_mortgage_out_form in land_mortgage_out_forms:
                if land_mortgage_out_form.is_valid() and land_mortgage_out_form.has_changed():
                    land_mortgage_out = land_mortgage_out_form.save(commit=False)
                    land_mortgage_out.household_number = household.get(request.session['household'])
                    land_mortgage_out.save()
                    form_land_mortgage_out_saved = True

            for lnd_lsd_in_shr_rent_form in lnd_lsd_in_shr_rent_forms:
                if lnd_lsd_in_shr_rent_form.is_valid() and lnd_lsd_in_shr_rent_form.has_changed():
                    lnd_lsd_in_shr_rent = lnd_lsd_in_shr_rent_form.save(commit=False)
                    lnd_lsd_in_shr_rent.household_number = household.get(request.session['household'])
                    lnd_lsd_in_shr_rent.save()
                    form_lnd_lsd_in_shr_rent_saved = True

            for lnd_lsd_out_shr_rent_form in lnd_lsd_out_shr_rent_forms:
                if lnd_lsd_out_shr_rent_form.is_valid() and lnd_lsd_out_shr_rent_form.has_changed():
                    lnd_lsd_out_shr_rent = lnd_lsd_out_shr_rent_form.save(commit=False)
                    lnd_lsd_out_shr_rent.household_number = household.get(request.session['household'])
                    lnd_lsd_out_shr_rent.save()
                    form_lnd_lsd_out_shr_rent_saved = True

            if form_land_mortgage_in_saved or form_land_mortgage_out_saved or form_land_mortgage_out_saved or form_lnd_lsd_out_shr_rent_saved:
                messages.success(request, 'Data saved successfully')

            return redirect('page4_edit', pk=request.session['household'])

    return render(request, 'page4.html', {'formset_lm_in': land_mortgage_in_formset(prefix='lm_in'),
                                          'formset_lm_out': land_mortgage_out_formset(prefix='lm_out'),
                                          'formset_lnd_lsd_in_shr_rent': lnd_lsd_in_shr_rent_formset(prefix='lnd_lsd_in_shr_rent'),
                                          'formset_lnd_lsd_out_shr_rent': lnd_lsd_out_shr_rent_formset(prefix='lnd_lsd_out_shr_rent'),
                                          'search_form': get_search_form()
                                          })


@login_required(login_url='login')
def edit(request, pk):
    #pdb.set_trace()
    try:
        request.session['household'] = pk  # TODO: temporary, remove when search functionality is implemented
        if request.method == "POST":
            land_mortgage_in_formset = formset_factory(LandMortgagedInForm, formset=BaseFormSet, extra=5)
            land_mortgage_in_forms = land_mortgage_in_formset(request.POST,prefix='lm_in')
            LandMortgagedIn.objects.filter(household_number=pk).delete()

            land_mortgage_out_formset = formset_factory(LandMortgagedOutForm, formset=BaseFormSet, extra=5)
            land_mortgage_out_forms = land_mortgage_out_formset(request.POST,prefix='lm_out')
            LandMortgagedOut.objects.filter(household_number=pk).delete()

            lnd_lsd_in_shr_rent_formset = formset_factory(LandLeasedInOnShareRentForm, formset=BaseFormSet, extra=5)
            lnd_lsd_in_shr_rent_forms = lnd_lsd_in_shr_rent_formset(request.POST, prefix='lnd_lsd_in_shr_rent')
            LandLeasedInOnShareRent.objects.filter(household_number=pk).delete()

            lnd_lsd_out_shr_rent_formset = formset_factory(LandLeasedOutOnShareRentForm, formset=BaseFormSet, extra=5)
            lnd_lsd_out_shr_rent_forms = lnd_lsd_out_shr_rent_formset(request.POST, prefix='lnd_lsd_out_shr_rent')
            LandLeasedOutOnShareRent.objects.filter(household_number=pk).delete()

            form_land_mortgage_in_saved = False
            form_land_mortgage_out_saved = False
            form_lnd_lsd_in_shr_rent_saved = False
            form_lnd_lsd_out_shr_rent_saved = False


            for land_mortgage_in_form in land_mortgage_in_forms:
                if land_mortgage_in_form.is_valid() and land_mortgage_in_form.has_changed():
                    land_mortgage_in = land_mortgage_in_form.save(commit=False)
                    land_mortgage_in.household_number = household.get(request.session['household'])
                    land_mortgage_in.save()
                    form_land_mortgage_in_saved = True


            for land_mortgage_out_form in land_mortgage_out_forms:
                if land_mortgage_out_form.is_valid() and land_mortgage_out_form.has_changed():
                    land_mortgage_out = land_mortgage_out_form.save(commit=False)
                    land_mortgage_out.household_number = household.get(request.session['household'])
                    land_mortgage_out.save()
                    form_land_mortgage_out_saved = True

            for lnd_lsd_in_shr_rent_form in lnd_lsd_in_shr_rent_forms:
                if lnd_lsd_in_shr_rent_form.is_valid() and lnd_lsd_in_shr_rent_form.has_changed():
                    lnd_lsd_in_shr_rent = lnd_lsd_in_shr_rent_form.save(commit=False)
                    lnd_lsd_in_shr_rent.household_number = household.get(request.session['household'])
                    lnd_lsd_in_shr_rent.save()
                    form_lnd_lsd_in_shr_rent_saved = True


            for lnd_lsd_out_shr_rent_form in lnd_lsd_out_shr_rent_forms:
                if lnd_lsd_out_shr_rent_form.is_valid() and lnd_lsd_out_shr_rent_form.has_changed():
                    lnd_lsd_out_shr_rent = lnd_lsd_out_shr_rent_form.save(commit=False)
                    lnd_lsd_out_shr_rent.household_number = household.get(request.session['household'])
                    lnd_lsd_out_shr_rent.save()
                    form_lnd_lsd_out_shr_rent_saved = True


            if form_land_mortgage_in_saved or form_land_mortgage_out_saved or form_land_mortgage_out_saved or form_lnd_lsd_out_shr_rent_saved:
                messages.success(request, 'Data saved successfully')


        land_mortgage_in_formset = modelformset_factory(LandMortgagedIn, form=LandMortgagedInForm, extra=5)
        result_set_lm_in = LandMortgagedIn.objects.filter(household_number=pk)
        formset_lm_in = land_mortgage_in_formset(prefix='lm_in',queryset=result_set_lm_in)

        land_mortgage_out_formset = modelformset_factory(LandMortgagedOut, form=LandMortgagedOutForm, extra=5)
        result_set_lm_out = LandMortgagedOut.objects.filter(household_number=pk)
        formset_lm_out = land_mortgage_out_formset(prefix='lm_out',queryset=result_set_lm_out)

        lnd_lsd_in_shr_rent_formset = modelformset_factory(LandLeasedInOnShareRent, form=LandLeasedInOnShareRentForm, extra=5)
        result_set_lnd_lsd_in_shr_rent = LandLeasedInOnShareRent.objects.filter(household_number=pk)
        formset_lnd_lsd_in_shr_rent = lnd_lsd_in_shr_rent_formset(prefix='lnd_lsd_in_shr_rent', queryset=result_set_lnd_lsd_in_shr_rent)

        lnd_lsd_out_shr_rent_formset = modelformset_factory(LandLeasedOutOnShareRent, form=LandLeasedOutOnShareRentForm,extra=5)
        result_set_lnd_lsd_out_shr_rent = LandLeasedOutOnShareRent.objects.filter(household_number=pk)
        formset_lnd_lsd_out_shr_rent = lnd_lsd_out_shr_rent_formset(prefix='lnd_lsd_out_shr_rent',queryset=result_set_lnd_lsd_out_shr_rent)

        return render(request, 'page4.html', {'formset_lm_in': formset_lm_in,
                                              'formset_lm_out': formset_lm_out,
                                              'formset_lnd_lsd_in_shr_rent': formset_lnd_lsd_in_shr_rent,
                                              'formset_lnd_lsd_out_shr_rent': formset_lnd_lsd_out_shr_rent,
                                              'search_form': get_search_form()})


    except Exception:
        return new(request)
