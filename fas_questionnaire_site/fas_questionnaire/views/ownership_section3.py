from ..forms.ownership_forms_section3 import CurrentOwnershipHoldingForm
from ..models.ownership_models_section3 import CurrentOwnershipHolding
from django.shortcuts import get_object_or_404, render, redirect
from . import household as household
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def init(request):
    if request.session.get('household') is None:
        return new(request)
    else:
        return edit(request, request.session['household'])


@login_required(login_url='login')
def new(request):
    if request.method == "POST":
        form = CurrentOwnershipHoldingForm(request.POST)
        if form.is_valid():
            ownership = form.save(commit=False)
            ownership.household = household.get(request.session['household'])
            ownership.save()
            return redirect('ownership_edit', pk=request.session['household'])
    else:
        form = CurrentOwnershipHoldingForm()
    return render(request, 'ownership_section3.html', {'ownership_form': form})


@login_required(login_url='login')
def edit(request, pk):
    try:
        request.session['household'] = pk  # TODO: temporary, remove when search functionality is implemented
        ownership = get_object_or_404(CurrentOwnershipHolding, household=pk)
        if request.method == "POST":
            form = CurrentOwnershipHoldingForm(request.POST, instance=ownership)
            if form.is_valid():
                ownership = form.save(commit=False)
                ownership.save()
                return redirect('ownership_edit', pk=pk)
        else:
            form = CurrentOwnershipHoldingForm(instance=ownership)
        return render(request, 'ownership_section3.html', {'ownership_form': form})
    except Exception:
        return new(request)


def get(household):
    try:
        ownership = CurrentOwnershipHolding.objects.get(household=household)
    except CurrentOwnershipHolding.DoesNotExist:
        ownership = None
    return ownership
