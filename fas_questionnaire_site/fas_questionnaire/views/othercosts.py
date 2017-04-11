from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.forms.formsets import formset_factory, BaseFormSet
from django.forms import modelformset_factory
from ..forms.othercosts import OtherCostsForm, OtherCostsExtraForm
from ..models.othercosts import OtherCosts
from ..models.household_models import Household


@login_required(login_url='login')
def init(request):
    if request.session.get('household') is None:
        return new(request)
    else:
        result_set = OtherCosts.objects.filter(household=request.session.get('household'))
        if len(result_set) == 0:
            return new(request)
        return edit(request, request.session['household'])


@login_required(login_url='login')
def new(request):
    crops_formset = formset_factory(OtherCostsForm, formset=BaseFormSet, extra=4)
    extra_formset = formset_factory(OtherCostsExtraForm, formset=BaseFormSet, extra=1)

    if request.method == "POST":
        other_form = OtherCostsForm(request.POST, prefix='form')
        crop_forms = crops_formset(request.POST, prefix='crop-form')
        extra_forms = extra_formset(request.POST, prefix='extra-form')

        if crop_forms.is_valid():
            for form in crop_forms:
                if form.is_valid() and form.has_changed():
                    record = form.save(commit=False)
                    record.household = Household.objects.get(pk=request.session['household'])
                    record.record_type = 0
                    record.save()
        if extra_forms.is_valid():
            for form in extra_forms:
                if form.is_valid() and form.has_changed():
                    record = form.save(commit=False)
                    if not record.amount_spent and not record.month_of_payment and not record.comments:
                        continue
                    record.household = Household.objects.get(pk=request.session['household'])
                    record.record_type = 1
                    record.save()
        if other_form.is_valid() and other_form.has_changed():
            record = other_form.save(commit=False)
            record.household = Household.objects.get(pk=request.session['household'])
            record.record_type = 2
            record.save()
        return redirect('othercosts_edit', pk= request.session['household'])

    return render(request, 'othercosts.html', {'crops_formset': crops_formset(prefix='crop-form'),
                                               'extra_formset': extra_formset(prefix='extra-form'),
                                               'form': OtherCostsForm(prefix='form')})


@login_required(login_url='login')
def edit(request, pk):
    if request.method == "POST":

        other_form = OtherCostsForm(request.POST, prefix='form')
        crop_forms = formset_factory(OtherCostsForm, formset=BaseFormSet)(request.POST, prefix='crop-form')
        extra_forms = formset_factory(OtherCostsExtraForm, formset=BaseFormSet)(request.POST, prefix='extra-form')
        OtherCosts.objects.filter(household=pk).delete()

        if crop_forms.is_valid():
            for form in crop_forms:
                if form.is_valid() and form.has_changed():
                    record = form.save(commit=False)
                    record.household = Household.objects.get(pk=pk)
                    record.record_type = 0
                    record.save()
        if extra_forms.is_valid():
            for form in extra_forms:
                if form.is_valid() and form.has_changed():
                    record = form.save(commit=False)
                    if not record.amount_spent and not record.month_of_payment and not record.comments:
                        continue
                    record.household = Household.objects.get(pk=pk)
                    record.record_type = 1
                    record.save()
        print(request.body)
        if other_form.is_valid() and other_form.has_changed():
            record = form.save(commit=False)
            record.household = Household.objects.get(pk=pk)
            record.record_type = 2
            record.save()

    crops_model_formset = modelformset_factory(OtherCosts,form=OtherCostsForm, extra=3)
    extra_model_formset = modelformset_factory(OtherCosts,form=OtherCostsExtraForm, extra=1)
    crops_result_set = OtherCosts.objects.filter(household=pk, record_type=0)
    extra_result_set = OtherCosts.objects.filter(household=pk, record_type=1)
    other_instance = OtherCosts.objects.filter(household=pk, record_type=2).first()
    crops_formset = crops_model_formset(queryset=crops_result_set, prefix='crop-form')
    extra_formset = extra_model_formset(queryset=extra_result_set, prefix='extra-form')
    return render(request, 'othercosts.html', {'crops_formset': crops_formset,
                                               'extra_formset': extra_formset,
                                               'form': OtherCostsForm(prefix='form', instance=other_instance)})
