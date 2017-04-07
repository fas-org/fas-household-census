from ..forms.ownership_wells_section9 import OwnershipWellsTubewellsForm
from ..models.ownership_wells_section9 import OwnershipWellsTubewells
from django.shortcuts import get_object_or_404, render, redirect
from . import household as household
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required(login_url='login')
def init(request):
    if request.session.get('household') is None:
        return new(request)
    else:
        return edit(request, request.session['household'])


@login_required(login_url='login')
def new(request):
    if request.method == "POST":
        form = OwnershipWellsTubewellsForm(request.POST)
        if form.is_valid():
            ownership = form.save(commit=False)
            ownership.household = household.get(request.session['household'])
            ownership.save()
            messages.success(request, 'Data saved successfully')
            return redirect('ownershipwells_edit', pk=request.session['household'])
    else:
        form = OwnershipWellsTubewellsForm()
    return render(request, 'ownership_wells_section9.html', {'ownership_form': form})


@login_required(login_url='login')
def edit(request, pk):
    try:
        request.session['household'] = pk  # TODO: temporary, remove when search functionality is implemented
        ownership = get_object_or_404(OwnershipWellsTubewells, household=pk)
        if request.method == "POST":
            form = OwnershipWellsTubewellsForm(request.POST, instance=ownership)
            if form.is_valid():
                ownership = form.save(commit=False)
                ownership.save()
                messages.success(request, 'Data saved successfully')
                return redirect('ownershipwells_edit', pk=pk)
        else:
            form = OwnershipWellsTubewellsForm(instance=ownership)
        return render(request, 'ownership_wells_section9.html', {'ownership_form': form})
    except Exception:
        return new(request)


def get(household):
    try:
        ownership = OwnershipWellsTubewells.objects.get(household=household)
    except OwnershipWellsTubewells.DoesNotExist:
        ownership = None
    return ownership
