from ..forms.land_lease_in_out_mortgage_forms_section5 import LandLeasedInOnFixedRentForm
from ..models.land_lease_in_out_mortgage_section5 import LandLeasedInOnFixedRent
from ..forms.land_lease_in_out_mortgage_forms_section5 import LandLeasedOutOnFixedRentForm
from ..models.land_lease_in_out_mortgage_section5 import LandLeasedOutOnFixedRent
from ..forms.land_lease_in_out_mortgage_forms_section5 import LandMortgagedInForm
from ..models.land_lease_in_out_mortgage_section5 import LandMortgagedIn
from ..forms.land_lease_in_out_mortgage_forms_section5 import LandMortgagedOutForm
from ..models.land_lease_in_out_mortgage_section5 import LandMortgagedOut
from django.shortcuts import get_object_or_404, render, redirect
from . import household as household
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.forms.formsets import formset_factory, BaseFormSet
from django.forms import modelformset_factory
import pdb

@login_required(login_url='login')
def init(request):
    #pdb.set_trace()
    if request.session.get('household') is None:
        return new(request)
    else:
        result_set_lnd_lsd_in_fxd_rnt = LandLeasedInOnFixedRent.objects.filter(household_number=request.session.get('household'))
        result_set_lnd_lsd_out_fxd_rnt = LandLeasedOutOnFixedRent.objects.filter(household_number=request.session.get('household'))
        result_set_LM_in = LandMortgagedIn.objects.filter(household_number=request.session.get('household'))
        result_set_LM_out = LandMortgagedOut.objects.filter(household_number=request.session.get('household'))

        if len(result_set_lnd_lsd_in_fxd_rnt) == 0 and \
                        len(result_set_lnd_lsd_out_fxd_rnt) == 0 and \
                        len(result_set_LM_in) == 0 and \
                        len(result_set_LM_out) == 0 :
            return new(request)
        return edit(request, request.session['household'])


@login_required(login_url='login')
def new(request):
    #pdb.set_trace()
    lnd_lsd_in_fxd_rnt_formset = formset_factory(LandLeasedInOnFixedRentForm, formset=BaseFormSet, extra=5)
    lnd_lsd_out_fxd_rnt_formset = formset_factory(LandLeasedOutOnFixedRentForm, formset=BaseFormSet, extra=5)
    land_mortgage_in_formset = formset_factory(LandMortgagedInForm, formset=BaseFormSet, extra=5)
    land_mortgage_out_formset = formset_factory(LandMortgagedOutForm, formset=BaseFormSet, extra=5)

    if request.method == "POST":
        lnd_lsd_in_fxd_rnt_forms = lnd_lsd_in_fxd_rnt_formset(request.POST, prefix='lnd_lsd_in_fxd_rnt')
        lnd_lsd_out_fxd_rnt_forms = lnd_lsd_out_fxd_rnt_formset(request.POST, prefix='lnd_lsd_out_fxd_rnt')
        land_mortgage_in_forms = land_mortgage_in_formset(request.POST, prefix='lm_in')
        land_mortgage_out_forms = land_mortgage_out_formset(request.POST, prefix='lm_out')

        form_lnd_lsd_in_fxd_rnt_saved = False
        form_lnd_lsd_out_fxd_rnt_saved = False
        form_land_mortgage_in_saved = False
        form_land_mortgage_out_saved = False

        if lnd_lsd_in_fxd_rnt_forms.is_valid() and \
                lnd_lsd_out_fxd_rnt_forms.is_valid() and \
                land_mortgage_in_forms.is_valid() and \
                land_mortgage_out_forms.is_valid() :
            for lnd_lsd_in_fxd_rnt_form in lnd_lsd_in_fxd_rnt_forms:
                if lnd_lsd_in_fxd_rnt_form.is_valid() and lnd_lsd_in_fxd_rnt_form.has_changed():
                    lnd_lsd_in_fxd_rnt = lnd_lsd_in_fxd_rnt_form.save(commit=False)
                    lnd_lsd_in_fxd_rnt.household_number = household.get(request.session['household'])
                    lnd_lsd_in_fxd_rnt.save()
                    form_lnd_lsd_in_fxd_rnt_saved = True

            for lnd_lsd_out_fxd_rnt_form in lnd_lsd_out_fxd_rnt_forms:
                if lnd_lsd_out_fxd_rnt_form.is_valid() and lnd_lsd_out_fxd_rnt_form.has_changed():
                    lnd_lsd_out_fxd_rnt = lnd_lsd_out_fxd_rnt_form.save(commit=False)
                    lnd_lsd_out_fxd_rnt.household_number = household.get(request.session['household'])
                    lnd_lsd_out_fxd_rnt.save()
                    form_lnd_lsd_out_fxd_rnt_saved = True

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

            if form_lnd_lsd_in_fxd_rnt_saved == True:
                messages.success(request, 'Data saved for land leased out fixed rent successfully')

            if form_lnd_lsd_out_fxd_rnt_saved == True:
                messages.success(request, 'Data saved for land leased in fixed rent successfully')


            if form_land_mortgage_in_saved == True:
                messages.success(request, 'Data saved for land mortgage in successfully')

            if form_land_mortgage_out_saved == True:
                messages.success(request, 'Data saved for land mortgage out successfully')


            return redirect('landleasemortgage_edit', pk=request.session['household'])

    return render(request, 'land_lease_in_out_mortgage_section5.html', {'formset_lnd_lsd_in_fxd_rnt': lnd_lsd_in_fxd_rnt_formset(prefix='lnd_lsd_in_fxd_rnt'),
                                                                        'formset_lnd_lsd_out_fxd_rnt': lnd_lsd_out_fxd_rnt_formset(prefix='lnd_lsd_out_fxd_rnt'),
                                                                        'formset_lm_in': land_mortgage_in_formset(prefix='lm_in'),
                                                                        'formset_lm_out': land_mortgage_out_formset(prefix='lm_out')
                                                                        })


@login_required(login_url='login')
def edit(request, pk):
    #pdb.set_trace()
    try:
        request.session['household'] = pk  # TODO: temporary, remove when search functionality is implemented
        if request.method == "POST":
            lnd_lsd_in_fxd_rnt_formset = formset_factory(LandLeasedInOnFixedRentForm, formset=BaseFormSet, extra=5)
            lnd_lsd_in_fxd_rnt_forms = lnd_lsd_in_fxd_rnt_formset(request.POST, prefix='lnd_lsd_in_fxd_rnt')
            LandLeasedInOnFixedRent.objects.filter(household_number=pk).delete()

            land_mortgage_in_formset = formset_factory(LandMortgagedInForm, formset=BaseFormSet, extra=5)
            land_mortgage_in_forms = land_mortgage_in_formset(request.POST,prefix='lm_in')
            LandMortgagedIn.objects.filter(household_number=pk).delete()

            land_mortgage_out_formset = formset_factory(LandMortgagedOutForm, formset=BaseFormSet, extra=5)
            land_mortgage_out_forms = land_mortgage_out_formset(request.POST,prefix='lm_out')
            LandMortgagedOut.objects.filter(household_number=pk).delete()

            lnd_lsd_out_fxd_rnt_formset = formset_factory(LandLeasedOutOnFixedRentForm, formset=BaseFormSet, extra=5)
            lnd_lsd_out_fxd_rnt_forms = lnd_lsd_out_fxd_rnt_formset(request.POST, prefix='lnd_lsd_out_fxd_rnt')
            LandLeasedOutOnFixedRent.objects.filter(household_number=pk).delete()

            form_lnd_lsd_in_fxd_rnt_saved = False
            form_lnd_lsd_out_fxd_rnt_saved = False
            form_land_mortgage_in_saved = False
            form_land_mortgage_out_saved = False

            for lnd_lsd_in_fxd_rnt_form in lnd_lsd_in_fxd_rnt_forms:
                if lnd_lsd_in_fxd_rnt_form.is_valid() and lnd_lsd_in_fxd_rnt_form.has_changed():
                    lnd_lsd_in_fxd_rnt = lnd_lsd_in_fxd_rnt_form.save(commit=False)
                    lnd_lsd_in_fxd_rnt.household_number = household.get(request.session['household'])
                    lnd_lsd_in_fxd_rnt.save()
                    form_lnd_lsd_in_fxd_rnt_saved = True

            for lnd_lsd_out_fxd_rnt_form in lnd_lsd_out_fxd_rnt_forms:
                if lnd_lsd_out_fxd_rnt_form.is_valid() and lnd_lsd_out_fxd_rnt_form.has_changed():
                    lnd_lsd_out_fxd_rnt = lnd_lsd_out_fxd_rnt_form.save(commit=False)
                    lnd_lsd_out_fxd_rnt.household_number = household.get(request.session['household'])
                    lnd_lsd_out_fxd_rnt.save()
                    form_lnd_lsd_out_fxd_rnt_saved = True



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

            if form_lnd_lsd_out_fxd_rnt_saved == True:
                messages.success(request, 'Data saved for land leased out fixed rent successfully')

            if form_lnd_lsd_in_fxd_rnt_saved == True:
                messages.success(request, 'Data saved for land leased in fixed rent successfully')

            if form_land_mortgage_in_saved == True:
                messages.success(request, 'Data saved land mortgage in successfully')

            if form_land_mortgage_out_saved == True:
                messages.success(request, 'Data saved land mortgage out successfully')


        lnd_lsd_in_fxd_rnt_formset = modelformset_factory(LandLeasedInOnFixedRent, form=LandLeasedInOnFixedRentForm, extra=5)
        result_set_lnd_lsd_in_fxd_rnt = LandLeasedInOnFixedRent.objects.filter(household_number=pk)
        formset_lnd_lsd_in_fxd_rnt = lnd_lsd_in_fxd_rnt_formset(prefix='lnd_lsd_in_fxd_rnt',queryset=result_set_lnd_lsd_in_fxd_rnt)

        lnd_lsd_out_fxd_rnt_formset = modelformset_factory(LandLeasedOutOnFixedRent, form=LandLeasedOutOnFixedRentForm, extra=5)
        result_set_lnd_lsd_out_fxd_rnt = LandLeasedOutOnFixedRent.objects.filter(household_number=pk)
        formset_lnd_lsd_out_fxd_rnt = lnd_lsd_out_fxd_rnt_formset(prefix='lnd_lsd_out_fxd_rnt',queryset=result_set_lnd_lsd_out_fxd_rnt)

        land_mortgage_in_formset = modelformset_factory(LandMortgagedIn, form=LandMortgagedInForm, extra=5)
        result_set_lm_in = LandMortgagedIn.objects.filter(household_number=pk)
        formset_lm_in = land_mortgage_in_formset(prefix='lm_in',queryset=result_set_lm_in)

        land_mortgage_out_formset = modelformset_factory(LandMortgagedOut, form=LandMortgagedOutForm, extra=5)
        result_set_lm_out = LandMortgagedOut.objects.filter(household_number=pk)
        formset_lm_out = land_mortgage_out_formset(prefix='lm_out',queryset=result_set_lm_out)

        return render(request, 'land_lease_in_out_mortgage_section5.html', {'formset_lnd_lsd_in_fxd_rnt': formset_lnd_lsd_in_fxd_rnt,
                                                                            'formset_lnd_lsd_out_fxd_rnt': formset_lnd_lsd_out_fxd_rnt,
                                                                            'formset_lm_in': formset_lm_in,
                                                                            'formset_lm_out': formset_lm_out,
                                                                            })

    except Exception:
        return new(request)


def get(household):
    try:
        land_leased_in_fixed_rent = LandLeasedInOnFixedRent.objects.get(household=household)
    except LandLeasedInOnFixedRent.DoesNotExist:
        land_leased_in_fixed_rent = None
    return land_leased_in_fixed_rent
