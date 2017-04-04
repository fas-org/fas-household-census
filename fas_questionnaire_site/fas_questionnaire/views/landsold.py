from ..forms import LandSoldForm
from ..models import LandSold
from django.shortcuts import get_object_or_404
from . import household


def new(request):
    if request.method == "POST":
        form = LandSoldForm(request.POST)
        if form.is_valid():
            landsoldform = form.save(commit=False)
            landsoldform.household = household.get(request.session['household'])
            landsoldform.save()
    else:
        form = LandSoldForm()
    return form


def update(request, pk):
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
        return new(request)


def save(form):
    if form.is_valid():
        form = form.save(commit=False)
        form.save()

#
# def get(household):
#     try:
#         introduction = HouseholdIntroduction.objects.get(household=household)
#     except HouseholdIntroduction.DoesNotExist:
#         introduction = None
#     return introduction