from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.forms import formset_factory, modelformset_factory, BaseFormSet
from ..forms.page19 import PublicDistributionSystemForm, WaterForDomesticUseForm, HousingForm, HousingCommentsForm
from ..models.page19 import PublicDistributionSystem, WaterForDomesticUse, Housing, HousingComments
from ..views.common import save_formset, save_form, get_object_or_none, get_search_form


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
        pds_form = PublicDistributionSystemForm(request.POST, prefix='pds')
        water_use_forms = formset_factory(WaterForDomesticUseForm, formset=BaseFormSet, extra=5)(request.POST, prefix='water')
        housing_forms = formset_factory(HousingForm, formset=BaseFormSet, extra=5)(request.POST, prefix='housing')
        comments_form = HousingCommentsForm(request.POST, prefix='comments')
        if save_form(pds_form, pk) and save_formset(water_use_forms, WaterForDomesticUse, pk) and \
                save_formset(housing_forms, Housing, pk) and save_form(comments_form, pk):
            messages.success(request, 'Data saved successfully')
        return redirect('page19_edit', pk)

    pds_instance = get_object_or_none(PublicDistributionSystem, pk)
    pds_form = PublicDistributionSystemForm(instance=pds_instance, prefix='pds')
    comments_instance = get_object_or_none(HousingComments, pk)
    comments_form = HousingCommentsForm(instance=comments_instance, prefix='comments')

    water_model_formset = modelformset_factory(WaterForDomesticUse, form=WaterForDomesticUseForm, extra=5)
    water_result_set = WaterForDomesticUse.objects.filter(household=pk)
    water_formset = water_model_formset(queryset=water_result_set, prefix='water')
    housing_model_formset = modelformset_factory(Housing, form=HousingForm, extra=5)
    housing_result_set = Housing.objects.filter(household=pk)
    housing_formset = housing_model_formset(queryset=housing_result_set, prefix='housing')
    return render(request, 'page19.html', {'pds_form': pds_form, 'water_formset': water_formset,
                                           'housing_formset': housing_formset, 'comments_form': comments_form,
                                           'search_form': get_search_form()})
