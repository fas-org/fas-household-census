from ..models.household_models import Household, Village
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
import re
from django.contrib import messages


def get_primary_key(village_name, household_number):
    try:
        village = Village.objects.get(id=village_name)
    except Village.DoesNotExist:
        return None

    try:
        household = Household.objects.get(village=village.id, household_number=household_number)
    except Household.DoesNotExist:
        return None

    return household.id


def search(request):
    household_number = request.POST.get('Household_number')
    village_name = request.POST.get('village')
    pk = get_primary_key(village_name, household_number)
    reobj = re.match(r'(/fas/)(.*)(/search/)', request.path, 0)
    requested_page = reobj.group(2) + "_edit"
    if pk is None:
        request.session['search_err_msg'] = 'There is no house hold data with the details that you have entered'
        return redirect('household_edit', pk=pk) # TODO: get user opinion on this.
    else:
        request.session['household'] = pk
        if request.session.get('search_err_msg') is not None:
            del request.session['search_err_msg']
        return redirect(requested_page, pk=pk)
        # TODO: set the session variable here instead of setting it in each edit view

