from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.forms import formset_factory, modelformset_factory, BaseFormSet
from ..forms.page1 import HouseholdIntroductionForm, HouseholdMembersForm
from ..models.page1 import HouseholdIntroduction, HouseholdMembers
from ..views.common import save_formset, save_form, get_object_or_none


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
        form = HouseholdIntroductionForm(request.POST, prefix='introduction')
        household_members_formset = formset_factory(HouseholdMembersForm, formset=BaseFormSet, extra=5)
        forms = household_members_formset(request.POST, prefix='members')
        if save_form(form, pk) or save_formset(forms, HouseholdMembers, pk):
            messages.success(request, 'Data saved successfully')
        return redirect('page1_edit', pk)

    introduction = get_object_or_none(HouseholdIntroduction, pk)
    form = HouseholdIntroductionForm(instance=introduction, prefix='introduction')

    household_members_model_formset = modelformset_factory(HouseholdMembers,form=HouseholdMembersForm, extra=5)
    result_set = HouseholdMembers.objects.filter(household=pk)
    formset = household_members_model_formset(queryset=result_set, prefix='members')
    return render(request, 'page1.html', {'introduction_form': form, 'formset': formset})
