from ..forms import HouseholdIntroductionForm
from django.http import HttpResponse
from ..models import HouseholdIntroduction
from django.shortcuts import get_object_or_404


def new(request):
    form = HouseholdIntroductionForm(request.POST)
    return save(form)


def update(request, pk):
    try:
        introduction = get_object_or_404(HouseholdIntroduction, pk=pk)
        form = HouseholdIntroductionForm(request.POST, instance=introduction)
        return save(form)
    except HouseholdIntroduction.DoesNotExist:
        return new(request)


def save(form):
    if form.is_valid():
        introduction = form.save(commit=False)
        introduction.save()
        return HttpResponse(introduction.id);
    else:
        return HttpResponse(0);


def get(household):
    try:
        introduction = HouseholdIntroduction.objects.get(household=household)
    except HouseholdIntroduction.DoesNotExist:
        introduction = None
    return introduction