from ..forms import HouseholdForm
from django.http import HttpResponse

def save(request):
    form = HouseholdForm(request.POST)
    if form.is_valid():
        household = form.save(commit=False)
        household.save()
        return HttpResponse(household.id)
    else:
        return HttpResponse(0)