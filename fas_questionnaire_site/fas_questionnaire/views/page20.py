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
import pdb


@login_required(login_url='login')
def init(request):
    if request.session.get('household') is None:
        return new(request)
    else:
        result_set_outstanding_loans = OutstandingLoans.objects.filter(household_number=request.session.get('household'))
        result_set_loans_brwd_lst_yr_and_paid = LoansBorrowedLastYearAndRepaid.objects.filter(household_number=request.session.get('household'))
        result_set_mem_shp_in_slf_hlp_grps = MembershipInSelfHelpGroups.objects.filter(household_number=request.session.get('household'))
        result_set_dtls_of_bank_pst_offc_of_the_household = DetailsOfBankPostofficeAccountOfTheHousehold.objects.filter(household_number=request.session.get('household'))

        if len(result_set_outstanding_loans) == 0 and \
           len(result_set_loans_brwd_lst_yr_and_paid) == 0 and \
           len(result_set_mem_shp_in_slf_hlp_grps) == 0 and \
           len(result_set_dtls_of_bank_pst_offc_of_the_household) == 0:
           return new(request)
        return edit(request, request.session['household'])


@login_required(login_url='login')
def new(request):
    outstanding_loans_formset = formset_factory(OutstandingLoansForm, formset=BaseFormSet, extra=5)
    loans_brwd_lst_yr_and_paid_formset = formset_factory(LoansBorrowedLastYearAndRepaidForm, formset=BaseFormSet, extra=5)
    mem_shp_in_slf_hlp_grps_formset = formset_factory(MembershipInSelfHelpGroupsForm, formset=BaseFormSet, extra=5)
    dtls_of_bank_pst_offc_of_the_household_formset = formset_factory(DetailsOfBankPostofficeAccountOfTheHouseholdForm, formset=BaseFormSet, extra=5)

    if request.method == "POST":
        outstanding_loans_forms = outstanding_loans_formset(request.POST, prefix='outstanding_loans')
        loans_brwd_lst_yr_and_paid_forms = loans_brwd_lst_yr_and_paid_formset(request.POST, prefix='loans_brwd_lst_yr_and_paid')
        mem_shp_in_slf_hlp_grps_forms = mem_shp_in_slf_hlp_grps_formset(request.POST, prefix='mem_shp_in_slf_hlp_grps')
        dtls_of_bank_pst_offc_of_the_household_forms = dtls_of_bank_pst_offc_of_the_household_formset(request.POST, prefix='dtls_of_bank_pst_offc_of_the_household')


        form_outstanding_loans_saved = False
        form_loans_brwd_lst_yr_and_paid_saved = False
        form_mem_shp_in_slf_hlp_grps_saved = False
        form_dtls_of_bank_pst_offc_of_the_household_saved = False

        if outstanding_loans_forms.is_valid() and \
                loans_brwd_lst_yr_and_paid_forms.is_valid() and \
                mem_shp_in_slf_hlp_grps_forms.is_valid() and \
                dtls_of_bank_pst_offc_of_the_household_forms.is_valid():

            for outstanding_loans_form in outstanding_loans_forms:
                if outstanding_loans_form.is_valid() and outstanding_loans_form.has_changed():
                    outstanding_loans = outstanding_loans_form.save(commit=False)
                    outstanding_loans.household_number = household.get(request.session['household'])
                    outstanding_loans.save()
                    form_outstanding_loans_saved = True

            for loans_brwd_lst_yr_and_paid_form in loans_brwd_lst_yr_and_paid_forms:
                if loans_brwd_lst_yr_and_paid_form.is_valid() and loans_brwd_lst_yr_and_paid_form.has_changed():
                    loans_brwd_lst_yr_and_paid = loans_brwd_lst_yr_and_paid_form.save(commit=False)
                    loans_brwd_lst_yr_and_paid.household_number = household.get(request.session['household'])
                    loans_brwd_lst_yr_and_paid.save()
                    loans_brwd_lst_yr_and_paid_saved = True

            for mem_shp_in_slf_hlp_grps_form in mem_shp_in_slf_hlp_grps_forms:
                if mem_shp_in_slf_hlp_grps_form.is_valid() and mem_shp_in_slf_hlp_grps_form.has_changed():
                    mem_shp_in_slf_hlp_grps = mem_shp_in_slf_hlp_grps_form.save(commit=False)
                    mem_shp_in_slf_hlp_grps.household_number = household.get(request.session['household'])
                    mem_shp_in_slf_hlp_grps.save()
                    mem_shp_in_slf_hlp_grps_saved = True

            for dtls_of_bank_pst_offc_of_the_household_form in dtls_of_bank_pst_offc_of_the_household_forms:
                if dtls_of_bank_pst_offc_of_the_household_form.is_valid() and dtls_of_bank_pst_offc_of_the_household_form.has_changed():
                    dtls_of_bank_pst_offc_of_the_household = dtls_of_bank_pst_offc_of_the_household_form.save(commit=False)
                    dtls_of_bank_pst_offc_of_the_household.household_number = household.get(request.session['household'])
                    dtls_of_bank_pst_offc_of_the_household.save()
                    dtls_of_bank_pst_offc_of_the_household_saved = True


            if form_outstanding_loans_saved == True:
                messages.success(request, 'Data saved for land mortgage in successfully')

            if form_loans_brwd_lst_yr_and_paid_saved == True:
                messages.success(request, 'Data saved for land mortgage out successfully')

            if form_mem_shp_in_slf_hlp_grps_saved == True:
                messages.success(request, 'Data saved for land leased in on share rent successfully')

            if form_dtls_of_bank_pst_offc_of_the_household_saved == True:
                messages.success(request, 'Data saved for land leased out on share rent successfully')


            return redirect('page20_edit', pk=request.session['household'])

    return render(request, 'page20.html', {'formset_outstanding_loans': outstanding_loans_formset(prefix='outstanding_loans'),
                                          'formset_loans_brwd_lst_yr_and_paid': loans_brwd_lst_yr_and_paid_formset(prefix='loans_brwd_lst_yr_and_paid'),
                                          'formset_mem_shp_in_slf_hlp_grps': mem_shp_in_slf_hlp_grps_formset(prefix='mem_shp_in_slf_hlp_grps'),
                                          'formset_dtls_of_bank_pst_offc_of_the_household': dtls_of_bank_pst_offc_of_the_household_formset(prefix='dtls_of_bank_pst_offc_of_the_household')
                                          })


@login_required(login_url='login')
def edit(request, pk):
    try:
        request.session['household'] = pk  # TODO: temporary, remove when search functionality is implemented
        if request.method == "POST":
            outstanding_loans_formset = formset_factory(OutstandingLoansForm, formset=BaseFormSet, extra=5)
            outstanding_loans_forms = outstanding_loans_formset(request.POST,prefix='outstanding_loans')
            OutstandingLoans.objects.filter(household_number=pk).delete()

            loans_brwd_lst_yr_and_paid_formset = formset_factory(LoansBorrowedLastYearAndRepaidForm, formset=BaseFormSet, extra=5)
            loans_brwd_lst_yr_and_paid_forms = loans_brwd_lst_yr_and_paid_formset(request.POST,prefix='loans_brwd_lst_yr_and_paid')
            LoansBorrowedLastYearAndRepaid.objects.filter(household_number=pk).delete()

            mem_shp_in_slf_hlp_grps_formset = formset_factory(MembershipInSelfHelpGroupsForm, formset=BaseFormSet, extra=5)
            mem_shp_in_slf_hlp_grps_forms = mem_shp_in_slf_hlp_grps_formset(request.POST, prefix='mem_shp_in_slf_hlp_grps')
            MembershipInSelfHelpGroups.objects.filter(household_number=pk).delete()

            dtls_of_bank_pst_offc_of_the_household_formset = formset_factory(DetailsOfBankPostofficeAccountOfTheHouseholdForm, formset=BaseFormSet, extra=5)
            dtls_of_bank_pst_offc_of_the_household_forms = dtls_of_bank_pst_offc_of_the_household_formset(request.POST, prefix='dtls_of_bank_pst_offc_of_the_household')
            DetailsOfBankPostofficeAccountOfTheHousehold.objects.filter(household_number=pk).delete()

            form_outstanding_loans_saved = False
            loans_brwd_lst_yr_and_paid_saved = False
            form_mem_shp_in_slf_hlp_grps_saved = False
            form_dtls_of_bank_pst_offc_of_the_household_saved = False


            for outstanding_loans_form in outstanding_loans_forms:
                if outstanding_loans_form.is_valid() and outstanding_loans_form.has_changed():
                    outstanding_loans = outstanding_loans_form.save(commit=False)
                    outstanding_loans.household_number = household.get(request.session['household'])
                    outstanding_loans.save()
                    form_outstanding_loans_saved = True


            for loans_brwd_lst_yr_and_paid_form in loans_brwd_lst_yr_and_paid_forms:
                if loans_brwd_lst_yr_and_paid_form.is_valid() and loans_brwd_lst_yr_and_paid_form.has_changed():
                    loans_brwd_lst_yr_and_paid = loans_brwd_lst_yr_and_paid_form.save(commit=False)
                    loans_brwd_lst_yr_and_paid.household_number = household.get(request.session['household'])
                    loans_brwd_lst_yr_and_paid.save()
                    form_loans_brwd_lst_yr_and_paid_saved = True

            for mem_shp_in_slf_hlp_grps_form in mem_shp_in_slf_hlp_grps_forms:
                if mem_shp_in_slf_hlp_grps_form.is_valid() and mem_shp_in_slf_hlp_grps_form.has_changed():
                    mem_shp_in_slf_hlp_grps = mem_shp_in_slf_hlp_grps_form.save(commit=False)
                    mem_shp_in_slf_hlp_grps.household_number = household.get(request.session['household'])
                    mem_shp_in_slf_hlp_grps.save()
                    form_mem_shp_in_slf_hlp_grps_saved = True


            for dtls_of_bank_pst_offc_of_the_household_form in dtls_of_bank_pst_offc_of_the_household_forms:
                if dtls_of_bank_pst_offc_of_the_household_form.is_valid() and dtls_of_bank_pst_offc_of_the_household_form.has_changed():
                    dtls_of_bank_pst_offc_of_the_household = dtls_of_bank_pst_offc_of_the_household_form.save(commit=False)
                    dtls_of_bank_pst_offc_of_the_household.household_number = household.get(request.session['household'])
                    dtls_of_bank_pst_offc_of_the_household.save()
                    form_dtls_of_bank_pst_offc_of_the_household_saved = True


            if form_outstanding_loans_saved == True:
                messages.success(request, 'Data saved land mortgage in successfully')

            if form_loans_brwd_lst_yr_and_paid_saved == True:
                messages.success(request, 'Data saved land mortgage out successfully')

            if form_mem_shp_in_slf_hlp_grps_saved == True:
                messages.success(request, 'Data saved for land leased in on share rent successfully')

            if form_dtls_of_bank_pst_offc_of_the_household_saved == True:
                messages.success(request, 'Data saved for land leased out on share rent successfully')


        outstanding_loans_formset = modelformset_factory(OutstandingLoans, form=OutstandingLoansForm, extra=5)
        result_set_outstanding_loans = OutstandingLoans.objects.filter(household_number=pk)
        formset_outstanding_loans = outstanding_loans_formset(prefix='outstanding_loans',queryset=result_set_outstanding_loans)

        loans_brwd_lst_yr_and_paid_formset = modelformset_factory(LoansBorrowedLastYearAndRepaid, form=LoansBorrowedLastYearAndRepaidForm, extra=5)
        result_set_loans_brwd_lst_yr_and_paid = LoansBorrowedLastYearAndRepaid.objects.filter(household_number=pk)
        formset_loans_brwd_lst_yr_and_paid = loans_brwd_lst_yr_and_paid_formset(prefix='loans_brwd_lst_yr_and_paid',queryset=result_set_loans_brwd_lst_yr_and_paid)

        mem_shp_in_slf_hlp_grps_formset = modelformset_factory(MembershipInSelfHelpGroups, form=MembershipInSelfHelpGroupsForm, extra=5)
        result_set_mem_shp_in_slf_hlp_grps = MembershipInSelfHelpGroups.objects.filter(household_number=pk)
        formset_mem_shp_in_slf_hlp_grps = mem_shp_in_slf_hlp_grps_formset(prefix='mem_shp_in_slf_hlp_grps', queryset=result_set_mem_shp_in_slf_hlp_grps)

        dtls_of_bank_pst_offc_of_the_household_formset = modelformset_factory(DetailsOfBankPostofficeAccountOfTheHousehold, form=DetailsOfBankPostofficeAccountOfTheHouseholdForm,extra=5)
        result_set_dtls_of_bank_pst_offc_of_the_household = DetailsOfBankPostofficeAccountOfTheHousehold.objects.filter(household_number=pk)
        formset_dtls_of_bank_pst_offc_of_the_household = dtls_of_bank_pst_offc_of_the_household_formset(prefix='dtls_of_bank_pst_offc_of_the_household',queryset=result_set_dtls_of_bank_pst_offc_of_the_household)

        return render(request, 'page20.html', {'formset_outstanding_loans': formset_outstanding_loans,
                                              'formset_loans_brwd_lst_yr_and_paid': formset_loans_brwd_lst_yr_and_paid,
                                              'formset_mem_shp_in_slf_hlp_grps': formset_mem_shp_in_slf_hlp_grps,
                                              'formset_dtls_of_bank_pst_offc_of_the_household': formset_dtls_of_bank_pst_offc_of_the_household})


    except Exception:
        return new(request)
