from ..forms.page3 import LandLeasedInOnFixedRentForm
from ..models.page3 import LandLeasedInOnFixedRent
from ..forms.page3 import LandLeasedOutOnFixedRentForm
from ..models.page3 import LandLeasedOutOnFixedRent
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
        result_set_lnd_lsd_in_fxd_rnt = LandLeasedInOnFixedRent.objects.filter(household_number=request.session.get('household'))
        result_set_lnd_lsd_out_fxd_rnt = LandLeasedOutOnFixedRent.objects.filter(household_number=request.session.get('household'))

        if len(result_set_lnd_lsd_in_fxd_rnt) == 0 and \
                        len(result_set_lnd_lsd_out_fxd_rnt) == 0 :
            return new(request)
        return edit(request, request.session['household'])


@login_required(login_url='login')
def new(request):
    #pdb.set_trace()
    lnd_lsd_in_fxd_rnt_formset = formset_factory(LandLeasedInOnFixedRentForm, formset=BaseFormSet, extra=5)
    lnd_lsd_out_fxd_rnt_formset = formset_factory(LandLeasedOutOnFixedRentForm, formset=BaseFormSet, extra=5)

    if request.method == "POST":
        lnd_lsd_in_fxd_rnt_forms = lnd_lsd_in_fxd_rnt_formset(request.POST, prefix='lnd_lsd_in_fxd_rnt')
        lnd_lsd_out_fxd_rnt_forms = lnd_lsd_out_fxd_rnt_formset(request.POST, prefix='lnd_lsd_out_fxd_rnt')

        form_lnd_lsd_in_fxd_rnt_saved = False
        form_lnd_lsd_out_fxd_rnt_saved = False

        if lnd_lsd_in_fxd_rnt_forms.is_valid() and \
                lnd_lsd_out_fxd_rnt_forms.is_valid() :
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

            if form_lnd_lsd_in_fxd_rnt_saved and form_lnd_lsd_out_fxd_rnt_saved :
                messages.success(request,'Data Saved Successfully')


            return redirect('page3_edit', pk=request.session['household'])

    return render(request, 'page3.html', {'formset_lnd_lsd_in_fxd_rnt': lnd_lsd_in_fxd_rnt_formset(prefix='lnd_lsd_in_fxd_rnt'),
                                          'formset_lnd_lsd_out_fxd_rnt': lnd_lsd_out_fxd_rnt_formset(prefix='lnd_lsd_out_fxd_rnt'),
                                          'search_form': get_search_form()
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

            lnd_lsd_out_fxd_rnt_formset = formset_factory(LandLeasedOutOnFixedRentForm, formset=BaseFormSet, extra=5)
            lnd_lsd_out_fxd_rnt_forms = lnd_lsd_out_fxd_rnt_formset(request.POST, prefix='lnd_lsd_out_fxd_rnt')
            LandLeasedOutOnFixedRent.objects.filter(household_number=pk).delete()

            form_lnd_lsd_in_fxd_rnt_saved = False
            form_lnd_lsd_out_fxd_rnt_saved = False

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

            if form_lnd_lsd_in_fxd_rnt_saved and form_lnd_lsd_out_fxd_rnt_saved :
                messages.success(request,'Data Saved Successfully')


        lnd_lsd_in_fxd_rnt_formset = modelformset_factory(LandLeasedInOnFixedRent, form=LandLeasedInOnFixedRentForm, extra=5)
        result_set_lnd_lsd_in_fxd_rnt = LandLeasedInOnFixedRent.objects.filter(household_number=pk)
        formset_lnd_lsd_in_fxd_rnt = lnd_lsd_in_fxd_rnt_formset(prefix='lnd_lsd_in_fxd_rnt', queryset=result_set_lnd_lsd_in_fxd_rnt)

        lnd_lsd_out_fxd_rnt_formset = modelformset_factory(LandLeasedOutOnFixedRent, form=LandLeasedOutOnFixedRentForm, extra=5)
        result_set_lnd_lsd_out_fxd_rnt = LandLeasedOutOnFixedRent.objects.filter(household_number=pk)
        formset_lnd_lsd_out_fxd_rnt = lnd_lsd_out_fxd_rnt_formset(prefix='lnd_lsd_out_fxd_rnt', queryset=result_set_lnd_lsd_out_fxd_rnt)

        return render(request, 'page3.html', {'formset_lnd_lsd_in_fxd_rnt': formset_lnd_lsd_in_fxd_rnt,
                                              'formset_lnd_lsd_out_fxd_rnt': formset_lnd_lsd_out_fxd_rnt,
                                              'search_form': get_search_form()
                                              })

    except Exception:
        return new(request)


def get(household):
    try:
        land_leased_in_fixed_rent = LandLeasedInOnFixedRent.objects.get(household=household)
    except LandLeasedInOnFixedRent.DoesNotExist:
        land_leased_in_fixed_rent = None
    return land_leased_in_fixed_rent
