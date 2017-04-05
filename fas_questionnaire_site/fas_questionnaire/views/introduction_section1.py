from ..forms import HouseholdIntroductionForm
from ..models import HouseholdIntroduction
from django.shortcuts import get_object_or_404, render, redirect
from . import household as household


def new(request):
    if request.method == "POST":
        form = HouseholdIntroductionForm(request.POST)
        if form.is_valid():
            introduction = form.save(commit=False)
            introduction.household = household.get(request.session['household'])
            introduction.save()
            return redirect('introduction_edit', pk=introduction.pk)
    else:
        form = HouseholdIntroductionForm()
    return render(request, 'introduction_section1.html', {'introduction_form': form})


def edit(request, pk):
    introduction = get_object_or_404(HouseholdIntroduction, pk=pk)
    if request.method == "POST":
        form = HouseholdIntroductionForm(request.POST, instance=introduction)
        if form.is_valid():
            introduction = form.save(commit=False)
            introduction.save()
            return redirect('introduction_edit', pk=pk)
    else:
        form = HouseholdIntroductionForm(instance=introduction)
    return render(request, 'introduction_section1.html', {'introduction_form': form})


def get(household):
    try:
        introduction = HouseholdIntroduction.objects.get(household=household)
    except HouseholdIntroduction.DoesNotExist:
        introduction = None
    return introduction
