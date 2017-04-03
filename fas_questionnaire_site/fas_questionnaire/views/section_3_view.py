from ..section_3_forms import CurrentOwnershipHoldingForm
from django.http import HttpResponse
from ..section_3_models import CurrentOwnershipHolding
from django.shortcuts import get_object_or_404


def new(request):
    form = CurrentOwnershipHoldingForm(request.POST)
    return save(form)


def update(request, pk):
    try:
        current_ownership_holding = get_object_or_404(CurrentOwnershipHolding, pk=pk)
        form = CurrentOwnershipHoldingForm(request.POST, instance=current_ownership_holding)
        return save(form)
    except CurrentOwnershipHolding.DoesNotExist:
        return new(request)


def save(form):
    if form.is_valid():
        current_ownership_holding = form.save(commit=False)
        current_ownership_holding.save()
        return HttpResponse(current_ownership_holding.id)
    else:
        return HttpResponse(0)


def get(household):
    try:
        current_ownership_holding = CurrentOwnershipHolding.objects.get(household=household)
    except CurrentOwnershipHolding.DoesNotExist:
        current_ownership_holding = None
    return current_ownership_holding
