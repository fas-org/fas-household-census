from functools import reduce

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.forms.formsets import formset_factory, BaseFormSet
from django.forms import modelformset_factory

from fas_questionnaire.views.common import get_object_or_none
from ..models.page7 import InputUseManure, InputUseSeeds, InputUsePlantProtectionIrrigation, InputUseFertiliser
from ..forms.page7 import InputUseForm, InputUseFertiliserForm, InputUseManureForm, InputUseSeedsForm, \
    InputUsePlantProtectionIrrigationForm
from ..models.household_models import Household


@login_required(login_url='login')
def init(request):
    if request.session.get('household') is None:
        return redirect('household_init')
    else:
        return edit(request, request.session['household'])


number_of_forms = 0


@login_required(login_url='login')
def edit(request, pk):
    global number_of_forms
    formset = formset_factory(InputUseForm, formset=BaseFormSet, extra=3)
    if request.method == 'POST':
        forms = formset(request.POST)
        number_of_forms = forms.__len__()
        if forms.is_valid():
            for form in forms:
                form.save(pk)

    formset_initial_data = collate_columns(pk, number_of_forms)
    if (len(formset_initial_data) > 0):
        formset = formset(formset_initial_data)
    # print("hi intital data " ,formset_initial_data)
    # print(type(formset_initial_data))
    # print("hi formset data ",formset)
    return render(request, 'page7.html', {'formset': formset})


def save_page7_form(form, household_id, model):
    if form.is_valid():
        if form.has_changed():
            record = form.save(commit=False)
            try:
                form_crop_code = form.data['crop_code']
                form_id = model.objects.get(crop_code=form_crop_code).id
            except Exception:
                form_id = None
            if form_id:
                record.id = int(form_id)
            record.household = get_object_or_none(Household, household_id)
            record.save()
            return True
        return True
    return False


def collate_columns(pk, number_of_forms):
    manure_resultset = InputUseManure.objects.filter(household=pk)
    fertiliser_resultset = InputUseFertiliser.objects.filter(household=pk)
    plant_protection_resultset = InputUsePlantProtectionIrrigation.objects.filter(household=pk)
    seeds_resultset = InputUseSeeds.objects.filter(household=pk)
    temp_data = [{'form-TOTAL_FORMS': number_of_forms, 'form-INITIAL_FORMS': '0', 'form-MIN_NUM_FORMS': '0',
                  'form-MAX_NUM_FORMS': '1000',
                  'form-' + str(counter) + '-crop_code': manure.crop_code,
                  'form-' + str(counter) + '-manure_type': manure.manure_type,
                  'form-' + str(counter) + '-manure_home_quantity': manure.manure_home_quantity,
                  'form-' + str(counter) + '-manure_home_unit': manure.manure_home_unit,
                  'form-' + str(counter) + '-manure_home_value': manure.manure_home_value,
                  'form-' + str(counter) + '-manure_purchased_quantity': manure.manure_purchased_quantity,
                  'form-' + str(counter) + '-manure_purchased_unit': manure.manure_purchased_unit,
                  'form-' + str(counter) + '-manure_purchased_price': manure.manure_purchased_price,

                  'form-' + str(counter) + '-plant_protection_quantity': plant.plant_protection_quantity,
                  'form-' + str(counter) + '-plant_protection_price': plant.plant_protection_price,
                  'form-' + str(counter) + '-irrigation_source': plant.irrigation_source,
                  'form-' + str(counter) + '-irrigation_price': plant.irrigation_price,

                  'form-' + str(counter) + '-fertiliser_type': fertiliser.fertiliser_type,
                  'form-' + str(counter) + '-fertiliser_quantity': fertiliser.fertiliser_quantity,
                  'form-' + str(counter) + '-fertiliser_price': fertiliser.fertiliser_price,

                  'form-' + str(counter) + '-home_produced_quantity': seed.home_produced_quantity,
                  'form-' + str(counter) + '-home_produced_value': seed.home_produced_value,
                  'form-' + str(counter) + '-purchased_quantity': seed.purchased_quantity,
                  'form-' + str(counter) + '-purchased_price': seed.purchased_price}
                 for counter, manure in enumerate(manure_resultset) for fertiliser in fertiliser_resultset for plant in
                 plant_protection_resultset for seed in seeds_resultset
                 if manure.crop_code == fertiliser.crop_code == plant.crop_code == seed.crop_code]

    data = dict(pair for data in temp_data for pair in data.items())

    return data

    # crop_code_set = set()
    # list = [x.crop_code for x in manure_resultset] + [x.crop_code for x in fertiliser_resultset] + [x.crop_code for x in plant_protection_resultset] + [x.crop_code for x in seeds_resultset]
    # for l in list:
    #     crop_code_set.add(l)
    # print(crop_code_set)
