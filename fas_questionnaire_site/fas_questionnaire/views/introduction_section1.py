from ..forms.introduction_forms_section1 import HouseholdIntroductionForm
from ..models.introduction_models_section1 import HouseholdIntroduction
from django.shortcuts import get_object_or_404, render, redirect
from . import household as household
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def init(request):
    if request.session.get('household') is None:
        return new(request)
    else:
        return edit(request, request.session['household'])


@login_required(login_url='login')
def new(request):
    if request.method == "POST":
        form = HouseholdIntroductionForm(request.POST)
        if form.is_valid():
            introduction = form.save(commit=False)
            introduction.household = household.get(request.session['household'])
            introduction.save()
            return redirect('introduction_edit', pk=request.session['household'])
    else:
        form = HouseholdIntroductionForm()
    return render(request, 'introduction_section1.html', {'introduction_form': form})


@login_required(login_url='login')
def edit(request, pk):
    try:
        request.session['household'] = pk  # TODO: temporary, remove when search functionality is implemented
        introduction = get_object_or_404(HouseholdIntroduction, household=pk)
        if request.method == "POST":
            form = HouseholdIntroductionForm(request.POST, instance=introduction)
            if form.is_valid():
                introduction = form.save(commit=False)
                introduction.save()
                return redirect('introduction_edit', pk=pk)
        else:
            form = HouseholdIntroductionForm(instance=introduction)
        return render(request, 'introduction_section1.html', {'introduction_form': form})
    except Exception:
        return new(request)


def get(household):
    try:
        introduction = HouseholdIntroduction.objects.get(household=household)
    except HouseholdIntroduction.DoesNotExist:
        introduction = None
    return introduction
