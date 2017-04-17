from ..forms.page2 import *
from ..models.page2 import *
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.forms.formsets import formset_factory, BaseFormSet
from django.forms import modelformset_factory
from .common import *


@login_required(login_url='login')
def init(request):
    if request.session.get('household') is None:
        return new(request)
    else:
        holding_result_set = CurrentOwnershipHolding.objects.filter(household=request.session.get('household'))
        homestead_area_result_set = HomesteadArea.objects.filter(household=request.session.get('household'))
        landsold_result_set = LandSold.objects.filter(household=request.session.get('household'))
        landpurchased_result_set = LandPurchased.objects.filter(household=request.session.get('household'))
        if len(holding_result_set) == 0 and len(homestead_area_result_set) == 0 and len(landsold_result_set) == 0 and len(landpurchased_result_set) == 0:
            return new(request)
        return edit(request, request.session['household'])


@login_required(login_url='login')
def new(request):
    current_ownership_formset = formset_factory(CurrentOwnershipHoldingForm, formset=BaseFormSet, extra=5)
    homestead_area_formset = formset_factory(HomesteadAreaForm, formset=BaseFormSet, extra=1)
    landsold_formset = formset_factory(LandSoldForm, formset=BaseFormSet, extra=5)
    landpurchased_formset = formset_factory(LandPurchasedForm, formset=BaseFormSet, extra=5)
    landpurchased_comments_form = LandPurchasedCommentsForm()
    if request.method == "POST":
        ownership_forms = current_ownership_formset(request.POST, prefix='owner')
        homestead_area_forms = homestead_area_formset(request.POST, prefix='homestead')
        landsoldforms = landsold_formset(request.POST, prefix='landsold')
        landpurchasedforms = landpurchased_formset(request.POST, prefix='landpurchased')
        landpurchased_comments_form = LandPurchasedCommentsForm(request.POST)
        if ownership_forms.is_valid() and homestead_area_forms.is_valid() and landsoldforms.is_valid() and landpurchasedforms.is_valid() and landpurchased_comments_form.is_valid():
            ownership_form_saved = save_forms(request, ownership_forms)
            homestead_form_saved = save_forms(request, homestead_area_forms)
            landsold_form_saved = save_forms(request, landsoldforms)
            landpurchased_form_saved = save_forms(request, landpurchasedforms)
            comments_form_saved = save_form_with_no_has_change(request, landpurchased_comments_form)

        if ownership_form_saved or homestead_form_saved or landsold_form_saved or landpurchased_form_saved or comments_form_saved:
            messages.success(request, 'Data saved successfully')
            return redirect('page2_edit', pk=request.session['household'])
        else:
            return render(request, 'page2.html',
                          {'current_ownership_formset': ownership_forms,
                           'homesteadformset': homestead_area_forms,
                           'landsold_formset': landsoldforms,
                           'landpurchased_formset': landpurchasedforms,
                           'landpurchased_comments_form': landpurchased_comments_form
                           })

    return render(request, 'page2.html', {'current_ownership_formset': current_ownership_formset(prefix='owner'),
                                          'homesteadformset': homestead_area_formset(prefix='homestead'),
                                          'landsold_formset': landsold_formset(prefix='landsold'),
                                          'landpurchased_formset': landpurchased_formset(prefix='landpurchased'),
                                          'landpurchased_comments_form': landpurchased_comments_form
                                          })


@login_required(login_url='login')
def edit(request, pk):
    try:
        request.session['household'] = pk  # TODO: temporary, remove when search functionality is implemented
        landpurchased_comments = get_object_or_404(LandPurchasedComments, household=pk)
        if request.method == "POST":

            current_ownership_formset = modelformset_factory(CurrentOwnershipHolding, form=CurrentOwnershipHoldingForm, extra=5)
            homestead_area_formset = modelformset_factory(HomesteadArea, form=HomesteadAreaForm, extra=1)
            landsold_formset = modelformset_factory(LandSold, form=LandSoldForm, extra=5)
            landpurchased_formset = modelformset_factory(LandPurchased, form=LandPurchasedForm, extra=5)

            ownership_forms = current_ownership_formset(request.POST, prefix='owner')
            homestead_area_forms = homestead_area_formset(request.POST, prefix='homestead')
            landsoldforms = landsold_formset(request.POST, prefix='landsold')
            landpurchasedforms = landpurchased_formset(request.POST, prefix='landpurchased')
            landpurchased_comments_form = LandPurchasedCommentsForm(request.POST, instance=landpurchased_comments)

            if ownership_forms.is_valid() and homestead_area_forms.is_valid() and landsoldforms.is_valid() and landpurchasedforms.is_valid() and landpurchased_comments_form.is_valid():
                ownership_form_saved = save_forms(request, ownership_forms)
                homestead_form_saved = save_forms(request, homestead_area_forms)
                landsold_form_saved = save_forms(request, landsoldforms)
                landpurchased_form_saved = save_forms(request, landpurchasedforms)
                comments_form_saved = save_form_with_no_has_change(request, landpurchased_comments_form)

            if ownership_form_saved or homestead_form_saved or landsold_form_saved or landpurchased_form_saved or comments_form_saved:
                messages.success(request, 'Data saved successfully')
            else:
                return render(request, 'page2.html',
                              {'current_ownership_formset': ownership_forms,
                               'homesteadformset': homestead_area_forms,
                               'landsold_formset': landsoldforms,
                               'landpurchased_formset': landpurchasedforms,
                               'landpurchased_comments_form': landpurchased_comments_form
                               })

        current_ownership_model_formset = modelformset_factory(CurrentOwnershipHolding,
                                                               form=CurrentOwnershipHoldingForm, extra=5)
        result_set = CurrentOwnershipHolding.objects.filter(household=pk)
        current_ownership_formset = current_ownership_model_formset(queryset=result_set, prefix='owner')

        homestead_area_model_formset = modelformset_factory(HomesteadArea, form=HomesteadAreaForm, extra=1)
        homestead_area_result_set = HomesteadArea.objects.filter(household=pk)
        homestead_area_formset = homestead_area_model_formset(queryset=homestead_area_result_set, prefix='homestead')

        landsold_model_formset = modelformset_factory(LandSold, form=LandSoldForm, extra=5)
        landsold_result_set = LandSold.objects.filter(household=pk)
        landsold_formset = landsold_model_formset(queryset=landsold_result_set, prefix='landsold')

        landpurchased_model_formset = modelformset_factory(LandPurchased, form=LandPurchasedForm, extra=5)
        landpurchased_result_set = LandPurchased.objects.filter(household=pk)
        landpurchased_formset = landpurchased_model_formset(queryset=landpurchased_result_set, prefix='landpurchased')

        landpurchased_comments_form = LandPurchasedCommentsForm(instance=landpurchased_comments)

        return render(request, 'page2.html', {'current_ownership_formset': current_ownership_formset,
                                              'homesteadformset': homestead_area_formset,
                                              'landsold_formset': landsold_formset,
                                              'landpurchased_formset': landpurchased_formset,
                                              'landpurchased_comments_form': landpurchased_comments_form
                                              })

    except Exception:
        return new(request)
