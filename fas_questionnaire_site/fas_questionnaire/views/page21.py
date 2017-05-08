from django.forms import formset_factory, BaseFormSet, modelformset_factory
from django.shortcuts import render, redirect
from django.contrib import messages
from ..forms.page21 import *
from .common import *


@login_required(login_url='login')
def init(request):
    if request.session.get('household') is None:
        return redirect('household_init')
    else:
        return edit(request, request.session['household'])


def save_formset_page21(forms, model, household_id,category):
    if forms.is_valid():
        active_ids = []
        for form in forms:
            try:
                form_id = form.data[form.prefix+'-id']
            except KeyError:
                form_id = None
            if form.is_valid() and form.has_changed():
                record = form.save(commit=False)
                if form_id:
                    record.id = int(form_id)
                record.household = get_object_or_none(Household, household_id)
                record.save()
                active_ids.append(record.id)
            else:
                if form_id:
                    active_ids.append(int(form_id))
        all_ids = list(model.objects.filter(household=household_id,type_of_asset__in=[x.id for x in AssetType.objects.filter( asset_category_id=AssetCategory.objects.get(asset_category=category).id)] ).values_list('id',flat=True))
        model.objects.filter(id__in=[ x for x in all_ids if x not in active_ids]).delete()
        return True
    return False



@login_required(login_url='login')
def edit(request, pk):
    request.session['household'] = pk  # TODO: temporary, remove when search functionality is implemented
    error = False
    if request.method == "POST":
        # assetLandRegistrationForm = AssetLandRegistrationForm(request.POST)
        immovables_form_set = formset_factory(ImmovableForm, formset=BaseFormSet, extra=5)
        meansOfTransport_form_set = formset_factory(MeansOfTransportForm, formset=BaseFormSet, extra=5)
        electricEquipments_form_set = formset_factory(ElectricEquipmentsForm, formset=BaseFormSet, extra=5)
        otherDomesticDurableGoods_form_set = formset_factory(OtherDomesticDurableGoodsForm, formset=BaseFormSet,
                                                             extra=5)
        furniture_form_set = formset_factory(FurnitureForm, formset=BaseFormSet, extra=5)
        inventories_form_set = formset_factory(InventoriesForm, formset=BaseFormSet, extra=5)
        miscellaneous_form_set = formset_factory(MiscellaneousForm, formset=BaseFormSet, extra=5)

        immovablesForms = immovables_form_set(request.POST, prefix='Immovables')
        meansOfTransportForms = meansOfTransport_form_set(request.POST, prefix='MeansOfTransport')
        furnitureForms = furniture_form_set(request.POST, prefix='Furniture')
        electricEquipmentsForms = electricEquipments_form_set(request.POST, prefix='ElectricEquipments')
        otherDomesticDurableGoodsForms = otherDomesticDurableGoods_form_set(request.POST,
                                                                            prefix='OtherDomesticDurableGoods')
        inventoriesForms = inventories_form_set(request.POST, prefix='Inventories')
        miscellaneousForms = miscellaneous_form_set(request.POST, prefix='Miscellaneous')
        assetLandRegistrationForm = AssetLandRegistrationForm(request.POST,prefix='registration')

        if save_formset_page21(immovablesForms, AssetOwnership, pk,'Immovables') and save_formset_page21(meansOfTransportForms, AssetOwnership,pk,'MeansOfTransport') and save_formset_page21(furnitureForms,AssetOwnership,pk,'Furniture') and \
                save_formset_page21(electricEquipmentsForms, AssetOwnership, pk,'ElectricEquipments') and save_formset_page21(otherDomesticDurableGoodsForms,AssetOwnership, pk,'OtherDomesticDurableGoods') and save_formset_page21(inventoriesForms, AssetOwnership, pk,'Inventories') and save_formset_page21(miscellaneousForms, AssetOwnership,pk,'Miscellaneous') and save_form(assetLandRegistrationForm, pk):
            messages.success(request, 'Data saved successfully')
            return redirect('page21_edit', pk)
        else:
            error = True
        return render(request, 'page21.html', {
            'immovables_form_set': immovablesForms,
            'meansoftransport_form_set': meansOfTransportForms,
            'furniture_form_set': furnitureForms,
            'electricEquipments_form_set': electricEquipmentsForms,
            'otherDomesticDurableGoods_form_set': otherDomesticDurableGoodsForms,
            'inventories_form_set': inventoriesForms,
            'miscellaneous_form_set': miscellaneousForms,
            'land_details': assetLandRegistrationForm,
            'search_form': get_search_form(),'all_formsets':error})



    assetLandRegistration = get_object_or_none(AssetLandRegistration, pk)
    assetLandRegistrationForm = AssetLandRegistrationForm(instance=assetLandRegistration,prefix='registration')

    immovables_model_form = modelformset_factory(AssetOwnership, form=ImmovableForm, extra=5)
    immovables_result_set = AssetOwnership.objects.filter(household=pk, type_of_asset__in=[x.id for x in AssetType.objects.filter( asset_category_id=AssetCategory.objects.get(asset_category="Immovables").id)])
    immovablesSet = immovables_model_form(queryset=immovables_result_set, prefix='Immovables')

    meansOfTransport_model_form = modelformset_factory(AssetOwnership, form=MeansOfTransportForm, extra=5)
    meansOfTransport_result_set = AssetOwnership.objects.filter(household=pk, type_of_asset__in=[x.id for x in
                                                                                                 AssetType.objects.filter(
                                                                                                     asset_category_id=AssetCategory.objects.get(
                                                                                                         asset_category="MeansOfTransport").id)])
    meansOfTransportSet = meansOfTransport_model_form(queryset=meansOfTransport_result_set,
                                                      prefix='MeansOfTransport')

    furniture_model_form = modelformset_factory(AssetOwnership, form=FurnitureForm, extra=5)
    furniture_result_set = AssetOwnership.objects.filter(household=pk, type_of_asset__in=[x.id for x in
                                                                                          AssetType.objects.filter(
                                                                                              asset_category_id=AssetCategory.objects.get(
                                                                                                  asset_category="Furniture").id)])
    furnitureSet = furniture_model_form(queryset=furniture_result_set, prefix='Furniture')

    electric_model_form = modelformset_factory(AssetOwnership, form=ElectricEquipmentsForm, extra=5)
    electric_result_set = AssetOwnership.objects.filter(household=pk, type_of_asset__in=[x.id for x in
                                                                                         AssetType.objects.filter(
                                                                                             asset_category_id=AssetCategory.objects.get(
                                                                                                 asset_category="ElectricEquipments").id)])
    electricSet = electric_model_form(queryset=electric_result_set, prefix='ElectricEquipments')

    domestic_model_form = modelformset_factory(AssetOwnership, form=OtherDomesticDurableGoodsForm, extra=5)
    domestic_result_set = AssetOwnership.objects.filter(household=pk, type_of_asset__in=[x.id for x in
                                                                                         AssetType.objects.filter(
                                                                                             asset_category_id=AssetCategory.objects.get(
                                                                                                 asset_category="OtherDomesticDurableGoods").id)])
    domesticSet = domestic_model_form(queryset=domestic_result_set, prefix='OtherDomesticDurableGoods')

    inventories_model_form = modelformset_factory(AssetOwnership, form=InventoriesForm, extra=5)
    inventories_result_set = AssetOwnership.objects.filter(household=pk, type_of_asset__in=[x.id for x in
                                                                                            AssetType.objects.filter(
                                                                                                asset_category_id=AssetCategory.objects.get(
                                                                                                    asset_category="Inventories").id)])
    inventoriesSet = inventories_model_form(queryset=inventories_result_set, prefix='Inventories')

    miscellaneous_model_form = modelformset_factory(AssetOwnership, form=MiscellaneousForm, extra=5)
    miscellaneous_result_set = AssetOwnership.objects.filter(household=pk, type_of_asset__in=[x.id for x in
                                                                                              AssetType.objects.filter(
                                                                                                  asset_category_id=AssetCategory.objects.get(
                                                                                                      asset_category="Miscellaneous").id)])
    miscellaneousSet = miscellaneous_model_form(queryset=miscellaneous_result_set, prefix='Miscellaneous')

    return render(request, 'page21.html', {'immovables_form_set': immovablesSet,
                                           'meansoftransport_form_set': meansOfTransportSet,
                                           'furniture_form_set': furnitureSet,
                                           'electricEquipments_form_set': electricSet,
                                           'otherDomesticDurableGoods_form_set': domesticSet,
                                           'inventories_form_set': inventoriesSet,
                                           'miscellaneous_form_set': miscellaneousSet,
                                           'land_details': assetLandRegistrationForm,
                                           'search_form': get_search_form(), 'all_formsets': error})
