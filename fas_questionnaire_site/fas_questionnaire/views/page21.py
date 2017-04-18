from django.forms import formset_factory, BaseFormSet, modelformset_factory
from django.shortcuts import get_object_or_404, render, redirect
from . import household as household
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from ..models.page21 import AssetOwnership
from ..forms.page21 import ImmovableForm


@login_required(login_url='login')
def init(request):
    if request.session.get('household') is None:
        return new(request)
    else:
        asset_ownership_result_set = AssetOwnership.objects.filter(household=request.session.get('household'))
        if len(asset_ownership_result_set) == 0:
            return new(request)
        return edit(request, request.session['household'])


@login_required(login_url='login')
def new(request):
    immovables_form_set = formset_factory(ImmovableForm, formset=BaseFormSet, extra=5)
    if request.method == "POST":
        immovablesForms = immovables_form_set(request.POST, prefix='immovables')

        assetOwnership_save = False
        if immovablesForms.is_valid():
            for immovablesForm in immovablesForms:

                if immovablesForm.is_valid() and immovablesForm.has_changed():
                    immovables = immovablesForm.save(commit=False)
                    immovables.household = household.get(request.session['household'])
                    immovables.save()
                    assetOwnership_save=True

            if assetOwnership_save:
                messages.success(request, 'Data saved successfully')
                return redirect('page21_edit', pk=request.session['household'])

    return render(request, 'page21.html',
                  {'immovables_form_set': immovables_form_set(prefix='immovables')})


@login_required(login_url='login')
def edit(request, pk):
    try:
        request.session['household'] = pk  # TODO: temporary, remove when search functionality is implemented

        if request.method == "POST":

            immovables_form_set = formset_factory(ImmovableForm, formset=BaseFormSet, extra=5)
            immovablesForms = immovables_form_set(request.POST, prefix='immovables')

            immovable_save = False
            if immovablesForms.is_valid():
                AssetOwnership.objects.filter(household=pk).delete()

                for immovablesForm in immovablesForms:
                    if immovablesForm.is_valid() and immovablesForm.has_changed():
                        immovables = immovablesForm.save(commit=False)
                        immovables.household = household.get(request.session['household'])
                        immovables.save()

            if immovable_save:
                messages.success(request, 'Data saved successfully')

        immovables_model_form = modelformset_factory(AssetOwnership,form=ImmovableForm,extra=5)
        immovables_result_set=AssetOwnership.objects.filter(household=pk)
        immovablesSet=immovables_model_form(queryset=immovables_result_set)

        return render(request, 'page21.html',
                      {'immovables_form_set': immovablesSet(prefix='immovables')
                       })
    except Exception:
        return new(request)


def get(household):
    try:
        assetOwnership = AssetOwnership.objects.get(household=household)

    except AssetOwnership.DoesNotExist:
        assetOwnership = None
    return assetOwnership
