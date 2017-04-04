from ..forms import HouseholdIntroductionForm
from ..models import HouseholdIntroduction
from django.shortcuts import get_object_or_404
from . import household


def new(request):
    if request.method == "POST":
        form = HouseholdIntroductionForm(request.POST)
        if form.is_valid():
            introduction = form.save(commit=False)
            introduction.household = household.get(request.session['household'])
            introduction.save()
    else:
        form = HouseholdIntroductionForm()
    return form


def update(request, pk):
    try:
        introduction = get_object_or_404(HouseholdIntroduction, household=pk)
        if request.method == "POST":
            form = HouseholdIntroductionForm(request.POST, instance=introduction)
            save(form)
        else:
            form = HouseholdIntroductionForm(instance=introduction)
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
