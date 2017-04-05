from ..forms import HouseholdForm
from ..models import Household
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required


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
            request.session['household'] = household.pk
            return redirect('household_edit', pk=household.pk)
    else:
        form = HouseholdForm()
    return render(request, 'household.html', {'household_form': form})


@login_required(login_url='login')
def edit(request, pk):
    request.session['household'] = pk  # TODO: temporary, remove when search functionality is implemented
    household = get_object_or_404(Household, pk=pk)
    if request.method == "POST":
        form = HouseholdForm(request.POST, instance=household)
        if form.is_valid():
            household = form.save(commit=False)
            household.save()
            return redirect('household_edit', pk=pk)
    else:
        form = HouseholdForm(instance=household)
    return render(request, 'household.html', {'household_form': form})


def get(pk):
    try:
        household = Household.objects.get(pk=pk)
    except Household.DoesNotExist:
        household = None
    return household
