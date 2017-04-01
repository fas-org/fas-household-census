from ..forms import HouseholdIntroductionForm
from ..models import HouseholdIntroduction
from django.shortcuts import get_object_or_404


def new(request):
    if request.method == "POST":
        form = HouseholdIntroductionForm(request.POST)
        save(form)
    else:
        form = HouseholdIntroductionForm()
    return form


def update(request, pk):
    try:
        introduction = get_object_or_404(HouseholdIntroduction, pk=pk)
        if request.method == "POST":
            form = HouseholdIntroductionForm(request.POST, instance=introduction)
            save(form)
        else:
            form = HouseholdIntroductionForm(instance=introduction)
        return form
    except HouseholdIntroduction.DoesNotExist:
        return new(request)


def save(form):
    if form.is_valid():
        form = form.save(commit=False)
        form.save()


def get(household):
    try:
        introduction = HouseholdIntroduction.objects.get(household=household)
    except HouseholdIntroduction.DoesNotExist:
        introduction = None
    return introduction
