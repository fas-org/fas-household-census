from ..forms import HouseholdForm
from ..models import Household
from django.shortcuts import get_object_or_404


def new(request):
    household_id = 0
    if request.method == "POST":
        form = HouseholdForm(request.POST)
        household_id = save(form)
    else:
        form = HouseholdForm()
    request.session['household'] = household_id
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
    except Exception:
        return new(request)


def save(form):
    if form.is_valid():
        new_object = form.save(commit=False)
        new_object.save()
        return new_object.pk


def get(pk):
    try:
        household = Household.objects.get(pk=pk)
    except Household.DoesNotExist:
        household = None
    return household
