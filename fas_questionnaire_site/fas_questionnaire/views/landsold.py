from ..forms import LandSoldForm
from ..models import LandSold
from django.shortcuts import get_object_or_404
from . import household, buyer


def new(request, buyer_id):
    if request.method == "POST":
        form = LandSoldForm(request.POST)
        if form.is_valid():
            landsoldform = form.save(commit=False)
            landsoldform.household = household.get(request.session['household'])
            landsoldform.buyer = buyer_id
            landsoldform.save()
    else:
        form = LandSoldForm()
    return form


def update(request, pk, buyer_id):
    try:
        landsoldform = get_object_or_404(LandSold, household=pk)
        if request.method == "POST":
            form = LandSoldForm(request.POST, instance=landsoldform)
            save(form)
        else:
            form = LandSoldForm(instance=landsoldform)
        return form
    # except HouseholdIntroduction.DoesNotExist:
    except Exception:
        return new(request, buyer_id)


def save(form):
    if form.is_valid():
        form = form.save(commit=False)
        form.save()
