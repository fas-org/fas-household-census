from ..forms import HouseholdForm
from django.http import HttpResponse
from ..models import Household
from django.shortcuts import get_object_or_404


def new(request):
    form = HouseholdForm(request.POST)
    return save(form)


def update(request, pk):
    try:
        household = get_object_or_404(Household, pk=pk)
        form = HouseholdForm(request.POST, instance=household)
        return save(form)
    except Household.DoesNotExist:
        return new(request)


def save(form):
    if form.is_valid():
        household = form.save(commit=False)
        household.save()
        return HttpResponse(household.id)
    else:
        return HttpResponse(0)


def get(pk):
    try:
        household = Household.objects.get(pk=pk)
    except Household.DoesNotExist:
        household = None
    return household