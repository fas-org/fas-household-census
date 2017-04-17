from ..forms.page1 import HouseholdIntroductionForm, HouseholdMembersForm
from ..models.page1 import HouseholdIntroduction, HouseholdMembers
from django.shortcuts import render, redirect
from ..models.household_models import Household
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.forms import formset_factory, modelformset_factory, BaseFormSet


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
        if form.is_valid():
            introduction = form.save(commit=False)
            id = form.data[form.prefix+'-id']
            if id:
                introduction.id = id
            introduction.household = Household.objects.get(pk=request.session['household'])
            introduction.save()

        household_members_formset = formset_factory(HouseholdMembersForm, formset=BaseFormSet, extra=5)
        forms = household_members_formset(request.POST, prefix='members')
        if forms.is_valid():
            active_ids = []
            for form in forms:
                id = form.data[form.prefix+'-id']
                if form.is_valid() and form.has_changed():
                    member = form.save(commit=False)
                    if id:
                        member.id = int(id)
                    member.household = Household.objects.get(pk=request.session['household'])
                    member.save()
                    active_ids.append(member.id)
                else:
                    if id:
                        active_ids.append(int(id))
            all_ids = list(HouseholdMembers.objects.filter(household=pk).values_list('id',flat=True))
            HouseholdMembers.objects.filter(id__in=[ x for x in all_ids if x not in active_ids]).delete()

        messages.success(request, 'Data saved successfully')
        return redirect('page1_edit', pk)

    introduction = get(pk)
    form = HouseholdIntroductionForm(instance=introduction, prefix='introduction')

    household_members_model_formset = modelformset_factory(HouseholdMembers,form=HouseholdMembersForm, extra=5)
    result_set = HouseholdMembers.objects.filter(household=pk)
    formset = household_members_model_formset(queryset=result_set, prefix='members')
    return render(request, 'page1.html', {'introduction_form': form, 'formset': formset})


def get(household):
    try:
        introduction = HouseholdIntroduction.objects.get(household=household)
    except HouseholdIntroduction.DoesNotExist:
        introduction = None
    return introduction
