from django.shortcuts import render
from ..forms import HouseholdIntroductionForm


def init(request):
    print(request)
    return render(request, 'home.html', {'introductionForm': HouseholdIntroductionForm()})
