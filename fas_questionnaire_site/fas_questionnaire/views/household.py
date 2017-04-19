from ..forms.household_forms import HouseholdForm
from ..models.household_models import Household
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib import messages


@login_required(login_url='login')
def init(request):
    if request.session.get('household') is None:
        return new(request)
    else:
        return edit(request, request.session['household'])


@login_required(login_url='login')
def new(request):
    if request.session.get('household') is not None:
        del request.session['household']
    if request.method == "POST":
        form = HouseholdForm(request.POST)
        if form.is_valid():
            household = form.save(commit=False)
            household.save()
            messages.success(request, 'Data saved successfully')
            request.session['household'] = household.pk
            return redirect('household_edit', pk=household.pk)
    else:
        form = HouseholdForm()
    return render(request, 'household.html', {'household_form': form})


@login_required(login_url='login')
def edit(request, pk):
    try:
        request.session['household'] = pk  # TODO: temporary, remove when search functionality is implemented
        household = get_object_or_404(Household, pk=pk)
        if request.method == "POST":
            form = HouseholdForm(request.POST, instance=household)
            if form.is_valid():
                household = form.save(commit=False)
                household.save()
                messages.success(request, 'Data saved successfully')
                return redirect('household_edit', pk=pk)
        else:
            form = HouseholdForm(instance=household)
        return render(request, 'household.html', {'household_form': form})
    except Exception:
        return new(request)


@login_required(login_url='login')
def submit_household(request):
    group = Group.objects.get(name='DataEntry')
    if group in request.user.groups.all():
        household = Household.objects.get(pk=request.session.get('household'))
        household.is_submitted = True
        household.save()
    del request.session['household']
    return redirect('household_init')


def get(pk):
    try:
        household = Household.objects.get(pk=pk)
    except Household.DoesNotExist:
        household = None
    return household
