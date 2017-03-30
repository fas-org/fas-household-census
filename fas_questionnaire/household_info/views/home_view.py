from django.shortcuts import render, get_object_or_404, redirect
from ..forms import HouseholdForm, HouseholdMembersForm


def init(request):
    household_intro_form = HouseholdForm()
    household_members_form = HouseholdMembersForm()
    return render(request, 'home.html', {'household_intro_form': household_intro_form, 'household_members_form': household_members_form})
