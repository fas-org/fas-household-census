from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.forms.formsets import formset_factory, BaseFormSet
from django.forms import modelformset_factory
from ..forms.page10 import OtherCostsForm, OtherCostsExtraForm
from ..models.page10 import OtherCosts
from ..models.household_models import Household
from ..models.page10 import PaymentsToManagersAndLongTermWorkers
from ..forms.page10 import PaymentsToManagersAndLongTermWorkersForm
from ..models.page10 import EmployManagerOrLongTermWorker
from ..forms.page10 import EmployManagerOrLongTermWorkerForm
from .common import *

@login_required(login_url='login')
def init(request):
    if request.session.get('household') is None:
        return redirect('household_init')
    else:
        return edit(request, request.session['household'])

@login_required(login_url='login')
def edit(request, pk):
    if request.method == "POST":

        other_form = OtherCostsForm(request.POST, prefix='other-form')
        crop_forms = formset_factory(OtherCostsForm, formset=BaseFormSet)(request.POST, prefix='crop-form')
        extra_forms = formset_factory(OtherCostsExtraForm, formset=BaseFormSet)(request.POST, prefix='extra-form')

        employ_form = EmployManagerOrLongTermWorkerForm(request.POST,prefix='employ-form')

        payment_forms = formset_factory(PaymentsToManagersAndLongTermWorkersForm,formset=BaseFormSet)(request.POST,prefix = 'payment-form')

        if crop_forms.is_valid():
            active_ids = []
            for form in crop_forms:
                try:
                    id = form.data[form.prefix+'-id']
                except KeyError:
                    id = None
                if form.is_valid() and form.has_changed():
                    record = form.save(commit=False)
                    if id:
                        record.id = int(id)
                    record.household = Household.objects.get(pk=pk)
                    record.record_type = 0
                    record.save()
                    active_ids.append(record.id)
                else:
                    if id:
                        active_ids.append(int(id))
            all_ids = list(OtherCosts.objects.filter(household=pk, record_type=0).values_list('id', flat=True))
            OtherCosts.objects.filter(id__in=[ x for x in all_ids if x not in active_ids]).delete()

        if extra_forms.is_valid():
            active_ids = []
            for form in extra_forms:
                try:
                    id = form.data[form.prefix+'-id']
                except KeyError:
                    id = None
                if form.is_valid() and form.has_changed():
                    record = form.save(commit=False)
                    if id:
                        record.id = int(id)
                    record.household = Household.objects.get(pk=pk)
                    record.record_type = 1
                    record.save()
                    active_ids.append(record.id)
                else:
                    if id:
                        active_ids.append(int(id))
            all_ids = list(OtherCosts.objects.filter(household=pk, record_type=1).values_list('id', flat=True))
            OtherCosts.objects.filter(id__in=[ x for x in all_ids if x not in active_ids]).delete()

        if other_form.is_valid() and other_form.has_changed():
            id = other_form.data[other_form.prefix+'-id']
            record = other_form.save(commit=False)
            if id:
                record.id = int(id)
            record.household = Household.objects.get(pk=pk)
            record.record_type = 2
            record.save()

        if employ_form.is_valid() and employ_form.has_changed():
            id = employ_form.data[employ_form.prefix+'-id']
            record = employ_form.save(commit=False)
            if id:
                record.id = int(id)
            record.household = Household.objects.get(pk=pk)
            record.save()

        if payment_forms.is_valid():
            active_ids = []
            for form in payment_forms:
                try:
                    id = form.data[form.prefix+'-id']
                except KeyError:
                    id = None
                if form.is_valid() and form.has_changed():
                    record=form.save(commit=False)
                    if id:
                        record.id = int(id)
                    record.household = Household.objects.get(pk=pk)
                    record.save()
                    active_ids.append(record.id)
                else:
                    if id:
                        active_ids.append(int(id))
            all_ids = list(PaymentsToManagersAndLongTermWorkers.objects.filter(household=pk).values_list('id', flat=True))
            PaymentsToManagersAndLongTermWorkers.objects.filter(id__in=[ x for x in all_ids if x not in active_ids]).delete()

        save_formset(get_comments_formset_to_save(request), Comments, pk, 10)

        messages.success(request, "Data saved successfully")

    crops_model_formset = modelformset_factory(OtherCosts,form=OtherCostsForm, extra=1)
    extra_model_formset = modelformset_factory(OtherCosts,form=OtherCostsExtraForm, extra=1)

    crops_result_set = OtherCosts.objects.filter(household=pk, record_type=0)
    extra_result_set = OtherCosts.objects.filter(household=pk, record_type=1)

    other_instance = OtherCosts.objects.filter(household=pk, record_type=2).first()
    payment_instance = EmployManagerOrLongTermWorker.objects.filter(household=pk).first()

    crops_formset = crops_model_formset(queryset=crops_result_set, prefix='crop-form')
    extra_formset = extra_model_formset(queryset=extra_result_set, prefix='extra-form')

    payment_model_formset=modelformset_factory(PaymentsToManagersAndLongTermWorkers,form=PaymentsToManagersAndLongTermWorkersForm, extra=1, widgets= get_household_members_as_widget(pk, 'name_of_worker'))
    payment_resultset = PaymentsToManagersAndLongTermWorkers.objects.filter(household=pk)
    payment_formset = payment_model_formset(queryset=payment_resultset,prefix='payment-form')
    return render(request, 'page10.html', {'crops_formset': crops_formset,
                                            'extra_formset': extra_formset,
                                            'other_form': OtherCostsForm(prefix='other-form', instance=other_instance),
                                            'payment_formset' : payment_formset,
                                            'employ_form' : EmployManagerOrLongTermWorkerForm(prefix='employ-form',instance=payment_instance),
                                            'search_form': get_search_form(),
                                            'comments': get_comments_formset(pk, 10)})
