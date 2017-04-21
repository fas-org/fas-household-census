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
                form.save()

    return render(request, 'page7.html', { 'formset': formset})
