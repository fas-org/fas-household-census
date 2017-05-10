from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.forms import formset_factory, modelformset_factory, BaseFormSet
from ..forms.page18 import *
from ..models.page18 import *
from ..models.common import Comments
from ..views.common import *

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
        asset_aquisition_formset = formset_factory(AcquisitionAndLossOfMajorAssetsForm, formset=BaseFormSet, extra=1)
        forms = asset_aquisition_formset(request.POST, prefix='assets')

        children_formset = formset_factory(ForChildrenOfAge616YearsForm, formset=BaseFormSet, extra=1)
        children_forms = children_formset(request.POST, prefix='children')

        if save_formset(forms, AcquisitionAndLossOfMajorAssets, pk) \
                and save_formset(children_forms, ForChildrenOfAge616Years, pk)\
                and save_formset(get_comments_formset_to_save(request), Comments, pk, 18):
            messages.success(request, 'Data saved successfully')
        return redirect('page18_edit', pk)

    asset_aquisition_model_formset = modelformset_factory(AcquisitionAndLossOfMajorAssets,
                                                          form=AcquisitionAndLossOfMajorAssetsForm, extra=1)
    result_set = AcquisitionAndLossOfMajorAssets.objects.filter(household=pk)
    formset = asset_aquisition_model_formset(queryset=result_set, prefix='assets')

    children_model_formset = modelformset_factory(ForChildrenOfAge616Years,form=ForChildrenOfAge616YearsForm,extra=1, widgets = get_household_members_as_widget(pk, 'name'))
    children_result_set=ForChildrenOfAge616Years.objects.filter(household=pk)
    children_formset=children_model_formset(queryset=children_result_set,prefix='children')

    return render(request, 'page18.html', {'asset_acquisition_formset': formset,
                                           'children_formset':children_formset,
                                           'search_form': get_search_form(),
                                           'comments': get_comments_formset(pk, 18)})
