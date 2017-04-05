from ..forms import LandBoughtForm
from ..models import LandBought
from django.shortcuts import get_object_or_404
from . import household


def new(request, seller_id):
    if request.method == "POST":
        form = LandBoughtForm(request.POST)
        if form.is_valid():
            landboughtform = form.save(commit=False)
            landboughtform.household = household.get(request.session['household'])
            landboughtform.seller = seller_id
            landboughtform.save()
    else:
        form = LandBoughtForm()
    return form


def update(request, pk, seller_id):
    try:
        landboughtform = get_object_or_404(LandBought, household=pk)
        if request.method == "POST":
            form = LandBoughtForm(request.POST, instance=landboughtform)
            save(form)
        else:
            form = LandBoughtForm(instance=landboughtform)
        return form
    # except HouseholdIntroduction.DoesNotExist:
    except Exception:
        return new(request, seller_id)


def save(form):
    if form.is_valid():
        form = form.save(commit=False)
        form.save()
