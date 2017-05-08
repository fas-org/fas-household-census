from ..forms.page4 import LandMortgagedInForm
from ..models.page4 import LandMortgagedIn
from ..forms.page4 import LandMortgagedOutForm
from ..models.page4 import LandMortgagedOut
from ..forms.page4 import LandLeasedInOnShareRentForm
from ..models.page4 import LandLeasedInOnShareRent
from ..forms.page4 import LandLeasedOutOnShareRentForm
from ..models.page4 import LandLeasedOutOnShareRent
from django.shortcuts import render, redirect
from django.contrib import messages
from .common import *


@login_required(login_url='login')
def init(request):
    if request.session.get('household') is None:
        return redirect('household_init')
    else:
        return edit(request, request.session['household'])


@login_required(login_url='login')
def edit(request, pk):
    request.session['household'] = pk  # TODO: temporary, remove when search functionality is implemented

    if request.method == "POST":
        land_mortgage_in_formset = formset_factory(LandMortgagedInForm, formset=BaseFormSet, extra=1)
        land_mortgage_out_formset = formset_factory(LandMortgagedOutForm, formset=BaseFormSet, extra=1)
        lnd_lsd_in_shr_rent_formset = formset_factory(LandLeasedInOnShareRentForm, formset=BaseFormSet, extra=1)
        lnd_lsd_out_shr_rent_formset = formset_factory(LandLeasedOutOnShareRentForm, formset=BaseFormSet, extra=1)

        land_mortgage_out_forms = land_mortgage_out_formset(request.POST, prefix='lm_out')
        lnd_lsd_in_shr_rent_forms = lnd_lsd_in_shr_rent_formset(request.POST, prefix='lnd_lsd_in_shr_rent')
        lnd_lsd_out_shr_rent_forms = lnd_lsd_out_shr_rent_formset(request.POST, prefix='lnd_lsd_out_shr_rent')
        land_mortgage_in_forms = land_mortgage_in_formset(request.POST, prefix='lm_in')

        if save_formset(land_mortgage_in_forms, LandMortgagedIn, pk) and save_formset(land_mortgage_out_forms,
                                                                                      LandMortgagedOut,
                                                                                      pk) and save_formset(
                lnd_lsd_in_shr_rent_forms, LandLeasedInOnShareRent, pk) and save_formset(lnd_lsd_out_shr_rent_forms,
                                                                                         LandLeasedOutOnShareRent, pk) \
                and save_formset(get_comments_formset_to_save(request), Comments, pk, 4):
            messages.success(request, 'Data saved successfully')
        return redirect('page4_edit', pk)

    land_mortgage_in_formset = modelformset_factory(LandMortgagedIn, form=LandMortgagedInForm, extra=1)
    result_set_lm_in = LandMortgagedIn.objects.filter(household=pk)
    formset_lm_in = land_mortgage_in_formset(prefix='lm_in', queryset=result_set_lm_in)
    land_mortgage_out_formset = modelformset_factory(LandMortgagedOut, form=LandMortgagedOutForm, extra=1)
    result_set_lm_out = LandMortgagedOut.objects.filter(household=pk)
    formset_lm_out = land_mortgage_out_formset(prefix='lm_out', queryset=result_set_lm_out)

    lnd_lsd_in_shr_rent_formset = modelformset_factory(LandLeasedInOnShareRent, form=LandLeasedInOnShareRentForm,
                                                       extra=1)
    result_set_lnd_lsd_in_shr_rent = LandLeasedInOnShareRent.objects.filter(household=pk)
    formset_lnd_lsd_in_shr_rent = lnd_lsd_in_shr_rent_formset(prefix='lnd_lsd_in_shr_rent',
                                                              queryset=result_set_lnd_lsd_in_shr_rent)

    lnd_lsd_out_shr_rent_formset = modelformset_factory(LandLeasedOutOnShareRent, form=LandLeasedOutOnShareRentForm,
                                                        extra=1)
    result_set_lnd_lsd_out_shr_rent = LandLeasedOutOnShareRent.objects.filter(household=pk)
    formset_lnd_lsd_out_shr_rent = lnd_lsd_out_shr_rent_formset(prefix='lnd_lsd_out_shr_rent',
                                                                queryset=result_set_lnd_lsd_out_shr_rent)

    return render(request, 'page4.html', {'formset_lm_in': formset_lm_in,
                                          'formset_lm_out': formset_lm_out,
                                          'formset_lnd_lsd_in_shr_rent': formset_lnd_lsd_in_shr_rent,
                                          'formset_lnd_lsd_out_shr_rent': formset_lnd_lsd_out_shr_rent,
                                          'search_form': get_search_form(),
                                          'comments': get_comments_formset(pk, 4)})
