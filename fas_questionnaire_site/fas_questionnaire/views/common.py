from . import household as household
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def save_form(request, form):
    form_saved = None
    if form.is_valid() and form.has_changed():
        form_saved = False
        fas_object = form.save(commit=False)
        fas_object.household = household.get(request.session['household'])
        fas_object.save()
        form_saved = True
    return form_saved


def save_forms(request, forms):
    form_saved = None
    for form in forms:
        if form.is_valid() and form.has_changed():
            form_saved = False
            fas_object = form.save(commit=False)
            fas_object.household = household.get(request.session['household'])
            fas_object.save()
            form_saved = True  # TODO: add proper check to verify if all forms are saved
    return form_saved