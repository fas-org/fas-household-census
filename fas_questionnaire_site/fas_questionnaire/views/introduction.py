from ..forms import HouseholdIntroductionForm
from django.http import HttpResponse

def save(request):
    form = HouseholdIntroductionForm(request.POST)
    if form.is_valid():
        introduction = form.save(commit=False)
        introduction.save()
        return HttpResponse('success');
    else:
        return HttpResponse('failed');