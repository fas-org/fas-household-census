from fas_questionnaire.views.common import save_formset, save_form, get_object_or_none, get_search_form
from ..forms.page5 import *
from ..models.page5 import *
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.forms.formsets import formset_factory, BaseFormSet
from django.contrib import messages
from django.forms import modelformset_factory


@login_required(login_url='login')
def init(request):
    if request.session.get('household') is None:
        return redirect('household_init')
    else:
        return edit(request, request.session['household'])


@login_required(login_url='login')
def edit(request, pk):
    request.session['household'] = pk
    if request.method == "POST":
        croppingPattern_formset = formset_factory(CroppingPatternAndCropScheduleForm, formset=BaseFormSet, extra=5)
        forms = croppingPattern_formset(request.POST, prefix='pattern')

        croppingPatternCommentsForm = CroppingPatternAndCropScheduleCommentsForm(request.POST, prefix='comments')
        if save_formset(forms, CroppingPatternAndCropSchedule, pk) and save_form(croppingPatternCommentsForm, pk):
            messages.success(request, 'Data saved successfully')
        return redirect('page5_edit', pk)

    croppingPattern_model_formset = modelformset_factory(CroppingPatternAndCropSchedule,
                                                         form=CroppingPatternAndCropScheduleForm, extra=5)
    result_set = CroppingPatternAndCropSchedule.objects.filter(household=pk)
    formset = croppingPattern_model_formset(queryset=result_set, prefix='pattern')

    comments = get_object_or_none(CroppingPatternAndCropScheduleComments, pk)
    comments_form = CroppingPatternAndCropScheduleCommentsForm(instance=comments, prefix='comments')

    return render(request, 'page5.html', {'production_and_sales_on_operational_holding_formset': formset,
                                          'production_and_sales_on_operational_holding_comment_form': comments_form,
                                          'search_form': get_search_form()})
