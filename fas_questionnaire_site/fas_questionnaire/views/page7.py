from functools import reduce

from django.forms import modelformset_factory
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.forms.formsets import formset_factory, BaseFormSet

from fas_questionnaire.models.page5 import CroppingPatternAndCropSchedule
from fas_questionnaire.views.common import save_formset
from ..forms.page7 import *
from ..models.common import Comments
from .common import get_search_form, get_comments_formset_to_save, get_comments_formset


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

        manure_formset = formset_factory(InputUseManureForm, formset=BaseFormSet, extra=1, min_num=1)
        seeds_formset = formset_factory(InputUseSeedsForm, formset=BaseFormSet, extra=1, min_num=1)
        plant_protection_formset = formset_factory(InputUsePlantProtectionForm, formset=BaseFormSet, extra=1, min_num=1)
        irrigation_formset = formset_factory(InputUseIrrigationForm, formset=BaseFormSet, extra=1, min_num=1)
        fertiliser_formset = formset_factory(InputUseFertiliserForm, formset=BaseFormSet, extra=1, min_num=1)

        manure_forms = manure_formset(request.POST, prefix='manure')
        seeds_forms = seeds_formset(request.POST, prefix='seeds')
        plant_protection_forms = plant_protection_formset(request.POST, prefix='plant_protection')
        irrigation_forms = irrigation_formset(request.POST, prefix='irrigation')
        fertiliser_forms = fertiliser_formset(request.POST, prefix='fertiliser')

        if save_formset(manure_forms, InputUseManure, pk) \
                and save_formset(seeds_forms, InputUseSeeds, pk) \
                and save_formset(plant_protection_forms, InputUsePlantProtection, pk) \
                and save_formset(fertiliser_forms, InputUseFertiliser, pk) \
                and save_formset(irrigation_forms,
                                 InputUseIrrigation, pk) \
                and save_formset(get_comments_formset_to_save(request), Comments, pk, 7):
            messages.success(request, 'Data saved successfully')
            return redirect('page7_edit', pk)

    manure_formset_factory = modelformset_factory(InputUseManure, form=InputUseManureForm, extra=1)
    result_set_manure = InputUseManure.objects.filter(household=pk)
    formset_manure = manure_formset_factory(prefix='manure', queryset=result_set_manure)

    seeds_formset_factory = modelformset_factory(InputUseSeeds, form=InputUseSeedsForm, extra=1)
    # result_set_seeds = InputUseSeeds.objects.filter(household=pk)
    result_set_seeds = CroppingPatternAndCropSchedule.objects.filter(household=pk).values('crop_number_first_digit','crop_number_second_digit')

    formset_seeds = seeds_formset_factory(prefix='seeds', queryset=result_set_seeds)

    plant_protection_formset_factory = modelformset_factory(InputUsePlantProtection, form=InputUsePlantProtectionForm,
                                                            extra=1)
    result_set_plant_protection = InputUsePlantProtection.objects.filter(household=pk)
    formset_plant_protection = plant_protection_formset_factory(prefix='plant_protection',
                                                                queryset=result_set_plant_protection)

    irrigation_formset_factory = modelformset_factory(InputUseIrrigation, form=InputUseIrrigationForm, extra=1)
    result_set_irrigation = InputUseIrrigation.objects.filter(household=pk)
    formset_irrigation = irrigation_formset_factory(prefix='irrigation', queryset=result_set_irrigation)

    fertiliser_formset_factory = modelformset_factory(InputUseFertiliser, form=InputUseFertiliserForm, extra=1)
    result_set_fertiliser = InputUseFertiliser.objects.filter(household=pk)
    formset_fertiliser = fertiliser_formset_factory(prefix='fertiliser', queryset=result_set_fertiliser)

    return render(request, 'page7.html', {'formset_manure': formset_manure,
                                          'formset_seeds': formset_seeds,
                                          'formset_plant_protection': formset_plant_protection,
                                          'formset_irrigation': formset_irrigation,
                                          'formset_fertiliser': formset_fertiliser,
                                          'search_form': get_search_form(),
                                          'comments': get_comments_formset(pk, 7)})
