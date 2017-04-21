from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.forms import formset_factory, modelformset_factory, BaseFormSet
from ..forms.page18 import *
from ..models.page18 import *
from ..views.common import save_formset


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
        asset_aquisition_formset = formset_factory(AcquisitionAndLossOfMajorAssetsForm, formset=BaseFormSet, extra=5)
        forms = asset_aquisition_formset(request.POST, prefix='assets')
        if save_formset(forms, AcquisitionAndLossOfMajorAssets, pk):
            messages.success(request, 'Data saved successfully')
        return redirect('page18_edit', pk)

    asset_aquisition_model_formset = modelformset_factory(AcquisitionAndLossOfMajorAssets,
                                                          form=AcquisitionAndLossOfMajorAssetsForm, extra=5)
    result_set = AcquisitionAndLossOfMajorAssets.objects.filter(household=pk)
    formset = asset_aquisition_model_formset(queryset=result_set, prefix='assets')
    return render(request, 'page18.html', {'asset_acquisition_formset': formset })
