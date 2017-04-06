from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
import json
from ..forms.householdmembers import HouseholdMembersForm
from ..models.householdmembers import HouseholdMembers
from . import household


@login_required(login_url='login')
def init(request):
    if request.session.get('household') is None:
        return new(request)
    else:
        return edit(request, request.session['household'])


@login_required(login_url='login')
def new(request):
    return render(request, 'householdmembers.html')


@login_required(login_url='login')
def edit(request, pk):
    return render(request, 'householdmembers.html')

@login_required(login_url='login')
def save(request):
    if request.method == "POST":
        posted_forms = request.POST.getlist('forms[]')
        for posted_form in posted_forms:
            form_data = json.loads(posted_form)
            form = HouseholdMembersForm(form_data)
            if form.is_valid():
                household_members = form.save(commit=False)
                household_members.household = household.get(request.session['household'])
                household_members.save()
        messages.success(request, "Records saved successfully")
        return redirect('householdmembers_edit', pk= request.session['household'])
