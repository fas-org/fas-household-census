from ..forms.page20 import OutstandingLoansForm
from ..models.page20 import OutstandingLoans
from ..forms.page20 import LoansBorrowedLastYearAndRepaidForm
from ..models.page20 import LoansBorrowedLastYearAndRepaid
from ..forms.page20 import MembershipInSelfHelpGroupsForm
from ..models.page20 import MembershipInSelfHelpGroups
from ..forms.page20 import DetailsOfBankPostofficeAccountOfTheHouseholdForm
from ..models.page20 import DetailsOfBankPostofficeAccountOfTheHousehold
from django.shortcuts import get_object_or_404, render, redirect
from . import household as household
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.forms.formsets import formset_factory, BaseFormSet
from django.forms import modelformset_factory
from .common import *


@login_required(login_url='login')
def init(request):
    if request.session.get('household') is None:
        return redirect('household_init')
    else:
        return edit(request, request.session['household'])


@login_required(login_url='login')
def edit(request, pk):
    request.session['household'] = pk
    if request.method == "POST":
        outstanding_loans_formset = formset_factory(OutstandingLoansForm, formset=BaseFormSet, extra=5)
        loans_brwd_lst_yr_and_paid_formset = formset_factory(LoansBorrowedLastYearAndRepaidForm, formset=BaseFormSet,
                                                             extra=5)
        mem_shp_in_slf_hlp_grps_formset = formset_factory(MembershipInSelfHelpGroupsForm, formset=BaseFormSet, extra=5)
        dtls_of_bank_pst_offc_of_the_household_formset = formset_factory(
            DetailsOfBankPostofficeAccountOfTheHouseholdForm, formset=BaseFormSet, extra=5)

        outstanding_loans_forms = outstanding_loans_formset(request.POST, prefix='outstanding_loans')
        loans_brwd_lst_yr_and_paid_forms = loans_brwd_lst_yr_and_paid_formset(request.POST,
                                                                              prefix='loans_brwd_lst_yr_and_paid')
        mem_shp_in_slf_hlp_grps_forms = mem_shp_in_slf_hlp_grps_formset(request.POST, prefix='mem_shp_in_slf_hlp_grps')
        dtls_of_bank_pst_offc_of_the_household_forms = dtls_of_bank_pst_offc_of_the_household_formset(request.POST,
                                                                                                      prefix='dtls_of_bank_pst_offc_of_the_household')

        if save_formset(outstanding_loans_forms, OutstandingLoans, pk) \
                and save_formset(loans_brwd_lst_yr_and_paid_forms, LoansBorrowedLastYearAndRepaid, pk) \
                and save_formset(mem_shp_in_slf_hlp_grps_forms, MembershipInSelfHelpGroups, pk) \
                and save_formset(dtls_of_bank_pst_offc_of_the_household_forms,
                                 DetailsOfBankPostofficeAccountOfTheHousehold, pk):
            messages.success(request, 'Data saved succesfully')
            return redirect('page20_edit', pk)

    outstanding_loans_formset = modelformset_factory(OutstandingLoans, form=OutstandingLoansForm, extra=5)
    result_set_outstanding_loans = OutstandingLoans.objects.filter(household=pk)
    formset_outstanding_loans = outstanding_loans_formset(prefix='outstanding_loans',
                                                          queryset=result_set_outstanding_loans)

    loans_brwd_lst_yr_and_paid_formset = modelformset_factory(LoansBorrowedLastYearAndRepaid,
                                                              form=LoansBorrowedLastYearAndRepaidForm, extra=5)
    result_set_loans_brwd_lst_yr_and_paid = LoansBorrowedLastYearAndRepaid.objects.filter(household=pk)
    formset_loans_brwd_lst_yr_and_paid = loans_brwd_lst_yr_and_paid_formset(prefix='loans_brwd_lst_yr_and_paid',
                                                                            queryset=result_set_loans_brwd_lst_yr_and_paid)

    mem_shp_in_slf_hlp_grps_formset = modelformset_factory(MembershipInSelfHelpGroups,
                                                           form=MembershipInSelfHelpGroupsForm, extra=5)
    result_set_mem_shp_in_slf_hlp_grps = MembershipInSelfHelpGroups.objects.filter(household=pk)
    formset_mem_shp_in_slf_hlp_grps = mem_shp_in_slf_hlp_grps_formset(prefix='mem_shp_in_slf_hlp_grps',
                                                                      queryset=result_set_mem_shp_in_slf_hlp_grps)

    dtls_of_bank_pst_offc_of_the_household_formset = modelformset_factory(DetailsOfBankPostofficeAccountOfTheHousehold,
                                                                          form=DetailsOfBankPostofficeAccountOfTheHouseholdForm,
                                                                          extra=5)
    result_set_dtls_of_bank_pst_offc_of_the_household = DetailsOfBankPostofficeAccountOfTheHousehold.objects.filter(
        household=pk)
    formset_dtls_of_bank_pst_offc_of_the_household = dtls_of_bank_pst_offc_of_the_household_formset(
        prefix='dtls_of_bank_pst_offc_of_the_household', queryset=result_set_dtls_of_bank_pst_offc_of_the_household)

    return render(request, 'page20.html', {'formset_outstanding_loans': formset_outstanding_loans,
                                           'formset_loans_brwd_lst_yr_and_paid': formset_loans_brwd_lst_yr_and_paid,
                                           'formset_mem_shp_in_slf_hlp_grps': formset_mem_shp_in_slf_hlp_grps,
                                           'formset_dtls_of_bank_pst_offc_of_the_household': formset_dtls_of_bank_pst_offc_of_the_household})
