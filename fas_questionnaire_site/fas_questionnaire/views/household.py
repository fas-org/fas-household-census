from ..forms import HouseholdForm
from ..models import Household
from django.shortcuts import get_object_or_404


def new(request):
    if request.method == "POST":
        form = HouseholdForm(request.POST)
        save(form)
    else:
        form = HouseholdForm()
    return form


def update(request, pk):
    try:
        household = get_object_or_404(Household, pk=pk)
        if request.method == "POST":
            form = HouseholdForm(request.POST, instance=household)
            save(form)
        else:
            form = HouseholdForm(instance=household)
        return form
    except Household.DoesNotExist:
        return new(request)


def save(form):
    if form.is_valid():
        form = form.save(commit=False)
        form.save()


def get(pk):
    try:
        household = Household.objects.get(pk=pk)
    except Household.DoesNotExist:
        household = None
    return household
