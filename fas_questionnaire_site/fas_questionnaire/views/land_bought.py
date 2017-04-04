from ..forms import LandBoughtForm
from django.http import HttpResponse
from ..models import LandBought
from django.shortcuts import get_object_or_404


def new(request):
    form = LandBoughtForm(request.POST)
    return save(form)


def update(request, pk):
    try:
        landbought = get_object_or_404(LandBought, pk=pk)
        form = LandBoughtForm(request.POST, instance=landbought)
        return save(form)
    except LandBought.DoesNotExist:
        return new(request)


def save(form):
    if form.is_valid():
        landbought = form.save(commit=False)
        landbought.save()
        return HttpResponse(landbought.id)
    else:
        return HttpResponse(0)


def get(household):
    try:
        landbought = LandBought.objects.get(household=household)
    except LandBought.DoesNotExist:
        landbought = None
    return landbought
