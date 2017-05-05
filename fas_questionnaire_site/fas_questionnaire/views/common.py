from . import household as household
from django.contrib.auth.decorators import login_required
from ..models.household_models import Household
from ..models.page1 import HouseholdMembers
from ..forms.household_forms import HouseholdForm
from django import forms
from ..forms.common import CommentsForm
from ..models.common import Comments
from django.forms import modelformset_factory


def save_form_old(request, form):
    form_saved = False
    if form.is_valid() and form.has_changed():
        form_saved = False
        fas_object = form.save(commit=False)
        fas_object.household = household.get(request.session['household'])
        fas_object.save()
        form_saved = True
    return form_saved


def save_form_with_no_has_change(request, form):
    form_saved = False
    if form.is_valid():
        form_saved = False
        fas_object = form.save(commit=False)
        fas_object.household = household.get(request.session['household'])
        fas_object.save()
        form_saved = True
    return form_saved


def save_forms(request, forms):
    form_saved = False
    for form in forms:
        if form.is_valid() and form.has_changed():
            form_saved = False
            fas_object = form.save(commit=False)
            fas_object.household = household.get(request.session['household'])
            fas_object.save()
            form_saved = True  # TODO: add proper check to verify if all forms are saved
    return form_saved


def save_formset(forms, model, household_id, **kwargs): #Pass key-word args for filter
    """add, update and delete models using formset"""
    if forms.is_valid():
        active_ids = []
        for form in forms:
            try:
                form_id = form.data[form.prefix+'-id']
            except KeyError:
                form_id = None
            if form.is_valid() and form.has_changed():
                record = form.save(commit=False)
                if form_id:
                    record.id = int(form_id)
                record.household = get_object_or_none(Household, household_id)
                record.save()
                active_ids.append(record.id)
            else:
                if form_id:
                    active_ids.append(int(form_id))
        all_ids = list(model.objects.filter(household=household_id, **kwargs).values_list('id',flat=True))
        model.objects.filter(id__in=[ x for x in all_ids if x not in active_ids]).delete()
        return True
    return False


def save_form(form, household_id):
    """add or update model using modelForm"""
    if form.is_valid():
        if form.has_changed():
            record = form.save(commit=False)
            try:
                if not form.prefix == None:
                    form_id = form.data[form.prefix+'-id']
                else:
                    form_id = None
            except KeyError:
                form_id = None
            if form_id:
                record.id = int(form_id)
            record.household = get_object_or_none(Household, household_id)
            record.save()
            return True
        return True
    return False


def get_object_or_none(model, household_id, **kwargs):
    """get model object or return None"""
    try:
        if model == Household:
            model_object = model.objects.get(pk=household_id, **kwargs)
        else:
            model_object = model.objects.get(household=household_id, **kwargs)
    except model.DoesNotExist:
        model_object = None
    return model_object


def is_empty(field):
    if field is None or field == '':
        return True
    else:
        return False

def get_search_form():
    return HouseholdForm()

def get_household_members(household_id):
    household_model = get_object_or_none(Household, household_id)
    return HouseholdMembers.objects.filter(household=household_model)

def get_household_members_as_widget(household_id, field_name):
    return { field_name : forms.Select(choices=([(c.id, c.name) for c in get_household_members(household_id)]))}

def get_comments_formset(household_id, page_no):
    comments_formset = modelformset_factory(Comments, form=CommentsForm, extra=1, min_num=1)
    comments_result_set = Comments.objects.filter(household_id=household_id, page_no=page_no)
    return comments_formset(queryset=comments_result_set, prefix='comments')