from ..forms.page3 import LandLeasedInOnFixedRentForm
from ..models.page3 import LandLeasedInOnFixedRent
from ..forms.page3 import LandLeasedOutOnFixedRentForm
from ..models.page3 import LandLeasedOutOnFixedRent
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

        lnd_lsd_in_fxd_rnt_formset = formset_factory(LandLeasedInOnFixedRentForm, formset=BaseFormSet, extra=1)
        lnd_lsd_in_fxd_rnt_forms = lnd_lsd_in_fxd_rnt_formset(request.POST, prefix='lnd_lsd_in_fxd_rnt')

        lnd_lsd_out_fxd_rnt_formset = formset_factory(LandLeasedOutOnFixedRentForm, formset=BaseFormSet, extra=1)
        lnd_lsd_out_fxd_rnt_forms = lnd_lsd_out_fxd_rnt_formset(request.POST, prefix='lnd_lsd_out_fxd_rnt')

        if save_formset(lnd_lsd_in_fxd_rnt_forms, LandLeasedInOnFixedRent, pk) and save_formset(lnd_lsd_out_fxd_rnt_forms,LandLeasedOutOnFixedRent,pk)\
                and save_formset(get_comments_formset_to_save(request), Comments, pk, 3):
            messages.success(request, 'Data saved successfully')
        return redirect('page3_edit', pk)

    lnd_lsd_in_fxd_rnt_formset = modelformset_factory(LandLeasedInOnFixedRent, form=LandLeasedInOnFixedRentForm,
                                                      extra=1)
    result_set_lnd_lsd_in_fxd_rnt = LandLeasedInOnFixedRent.objects.filter(household=pk)
    formset_lnd_lsd_in_fxd_rnt = lnd_lsd_in_fxd_rnt_formset(prefix='lnd_lsd_in_fxd_rnt',
                                                            queryset=result_set_lnd_lsd_in_fxd_rnt)

    lnd_lsd_out_fxd_rnt_formset = modelformset_factory(LandLeasedOutOnFixedRent, form=LandLeasedOutOnFixedRentForm,
                                                       extra=1)
    result_set_lnd_lsd_out_fxd_rnt = LandLeasedOutOnFixedRent.objects.filter(household=pk)
    formset_lnd_lsd_out_fxd_rnt = lnd_lsd_out_fxd_rnt_formset(prefix='lnd_lsd_out_fxd_rnt',
                                                              queryset=result_set_lnd_lsd_out_fxd_rnt)

    return render(request, 'page3.html', {'formset_lnd_lsd_in_fxd_rnt': formset_lnd_lsd_in_fxd_rnt,
                                          'formset_lnd_lsd_out_fxd_rnt': formset_lnd_lsd_out_fxd_rnt,
                                          'search_form': get_search_form(),
                                          'comments': get_comments_formset(pk, 3)})
