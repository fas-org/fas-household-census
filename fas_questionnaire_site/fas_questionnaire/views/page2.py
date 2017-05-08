from ..forms.page2 import *
from ..models.page2 import *
from django.shortcuts import render, redirect
from django.contrib import messages
from django.forms.formsets import formset_factory, BaseFormSet
from django.forms import modelformset_factory
from .common import *


@login_required(login_url='login')
def init(request):
    if request.session.get('household') is None:
        return redirect('household_edit')
    else:
        return edit(request, request.session['household'])


@login_required(login_url='login')
def edit(request, pk):
    request.session['household'] = pk
    if request.method == "POST":
        current_ownership_formset = formset_factory(CurrentOwnershipHoldingForm, formset=BaseFormSet, extra=1)
        homestead_area_formset = formset_factory(HomesteadAreaForm, formset=BaseFormSet, extra=1)
        landsold_formset = formset_factory(LandSoldForm, formset=BaseFormSet, extra=1)
        landpurchased_formset = formset_factory(LandPurchasedForm, formset=BaseFormSet, extra=1)

        ownership_forms = current_ownership_formset(request.POST, prefix='owner')
        homestead_area_forms = homestead_area_formset(request.POST, prefix='homestead')
        landsoldforms = landsold_formset(request.POST, prefix='landsold')
        landpurchasedforms = landpurchased_formset(request.POST, prefix='landpurchased')

        if (save_formset(ownership_forms, CurrentOwnershipHolding, pk) and save_formset(homestead_area_forms, HomesteadArea, pk)
            and save_formset(landsoldforms, LandSold, pk) and save_formset(landpurchasedforms, LandPurchased, pk)
            and save_formset(get_comments_formset_to_save(request), Comments, pk, 2)):
            messages.success(request, "Data saved successfully")
            return redirect('page2_edit', pk)
        else:
            return render(request, 'page2.html', {'current_ownership_formset': ownership_forms,
                                                  'homesteadformset': homestead_area_forms,
                                                  'landsold_formset': landsoldforms,
                                                  'landpurchased_formset': landpurchasedforms,
                                                  'search_form': get_search_form(),
                                                  'comments': get_comments_formset(pk, 2)
                                                  })


    current_ownership_model_formset = modelformset_factory(CurrentOwnershipHolding,
                                                           form=CurrentOwnershipHoldingForm, extra=1)
    result_set = CurrentOwnershipHolding.objects.filter(household=pk)
    current_ownership_formset = current_ownership_model_formset(queryset=result_set, prefix='owner')

    homestead_area_model_formset = modelformset_factory(HomesteadArea, form=HomesteadAreaForm, extra=1)
    homestead_area_result_set = HomesteadArea.objects.filter(household=pk)
    homestead_area_formset = homestead_area_model_formset(queryset=homestead_area_result_set, prefix='homestead')

    landsold_model_formset = modelformset_factory(LandSold, form=LandSoldForm, extra=1)
    landsold_result_set = LandSold.objects.filter(household=pk)
    landsold_formset = landsold_model_formset(queryset=landsold_result_set, prefix='landsold')

    landpurchased_model_formset = modelformset_factory(LandPurchased, form=LandPurchasedForm, extra=1)
    landpurchased_result_set = LandPurchased.objects.filter(household=pk)
    landpurchased_formset = landpurchased_model_formset(queryset=landpurchased_result_set, prefix='landpurchased')

    return render(request, 'page2.html', {'current_ownership_formset': current_ownership_formset,
                                          'homesteadformset': homestead_area_formset,
                                          'landsold_formset': landsold_formset,
                                          'landpurchased_formset': landpurchased_formset,
                                          'search_form': get_search_form(),
                                          'comments': get_comments_formset(pk, 2)
                                          })