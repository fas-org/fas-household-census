from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.forms.formsets import formset_factory, BaseFormSet
from django.forms import modelformset_factory
from ..models.page7 import InputUseManure,InputUseSeeds,InputUsePlantProtectionIrrigation,InputUseFertiliser
from ..forms.page7 import InputUseForm, InputUseFertiliserForm,InputUseManureForm,InputUseSeedsForm,InputUsePlantProtectionIrrigationForm
from ..models.household_models import Household


@login_required(login_url='login')
def init(request):
    if request.session.get('household') is None:
        return redirect('household_init')
    else:
        return edit(request, request.session['household'])


@login_required(login_url='login')
def edit(request,pk):

    formset = formset_factory(InputUseForm,formset=BaseFormSet,extra=3)
    if request.method == 'POST':
        forms = formset(request.POST)
        if forms.is_valid():
            for form in forms:
                form.save(pk)

    formset_initial_data = collate_columns(pk)
    print(formset_initial_data)
    return render(request, 'page7.html', { 'formset': formset_initial_data})

def collate_columns(pk):
    manure_resultset = InputUseManure.objects.filter(household=pk)
    fertiliser_resultset = InputUseFertiliser.objects.filter(household=pk)
    plant_protection_resultset = InputUsePlantProtectionIrrigation.objects.filter(household=pk)
    seeds_resultset = InputUseSeeds.objects.filter(household=pk)
    data = [{'crop_code': manure.crop_code,
    'manure_type': manure.manure_type,
    'manure_home_quantity': manure.manure_home_quantity,
    'manure_home_unit': manure.manure_home_unit,
    'manure_home_value': manure.manure_home_value,
    'manure_purchased_quantity': manure.manure_purchased_quantity,
    'manure_purchased_unit': manure.manure_purchased_unit,
    'manure_purchased_price': manure.manure_purchased_price,

    'plant_protection_quantity': plant.plant_protection_quantity,
    'plant_protection_price': plant.plant_protection_price,
    'irrigation_source': plant.irrigation_source,
    'irrigation_price': plant.irrigation_price,

    'fertiliser_type': fertiliser.fertiliser_type,
    'fertiliser_quantity': fertiliser.fertiliser_quantity,
    'fertiliser_price': fertiliser.fertiliser_price,

    'home_produced_quantity': seed.home_produced_quantity,
    'home_produced_value': seed.home_produced_value,
    'purchased_quantity': seed.purchased_quantity,
    'purchased_price': seed.purchased_price }
     for manure in manure_resultset for fertiliser in fertiliser_resultset for plant in plant_protection_resultset for seed in seeds_resultset
     if manure.crop_code == fertiliser.crop_code == plant.crop_code == seed.crop_code ]
    return data

    # crop_code_set = set()
    # list = [x.crop_code for x in manure_resultset] + [x.crop_code for x in fertiliser_resultset] + [x.crop_code for x in plant_protection_resultset] + [x.crop_code for x in seeds_resultset]
    # for l in list:
    #     crop_code_set.add(l)
    # print(crop_code_set)
