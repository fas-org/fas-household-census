from ..forms.page5 import *
from ..models.page5 import *
from django.shortcuts import get_object_or_404, render, redirect
from . import household as household
from django.contrib.auth.decorators import login_required
from django.forms.formsets import formset_factory, BaseFormSet
from django.contrib import messages
from django.forms import modelformset_factory
from .common import *


@login_required(login_url='login')
def init(request):
    if request.session.get('household') is None:
        return new(request)
    else:
        croppingPattern_result_set=CroppingPatternAndCropSchedule.objects.filter(household=request.session.get('household'))
        comments_result_set=CroppingPatternAndCropScheduleComments.objects.filter(household=request.session.get('household'))
        if len(croppingPattern_result_set) == 0 and comments_result_set == 0:
            return new(request)
        return edit(request, request.session['household'])


@login_required(login_url='login')
def new(request):
    croppingPattern_formset = formset_factory(CroppingPatternAndCropScheduleForm, formset=BaseFormSet, extra=5)
    croppingPatternCommentsForm = CroppingPatternAndCropScheduleCommentsForm()

    if request.method == "POST":
        croppingPatternForms = croppingPattern_formset(request.POST)
        croppingPatternCommentsForm = CroppingPatternAndCropScheduleCommentsForm(request.POST)

        crop_patterns_saved = False
        crop_patterns_comments_saved = False
        if croppingPatternForms.is_valid() and croppingPatternCommentsForm.is_valid():
            crop_patterns_saved = save_forms(request, croppingPatternForms)
            crop_patterns_comments_saved = save_form_with_no_has_change(request, croppingPatternCommentsForm)

        if crop_patterns_saved or crop_patterns_comments_saved:
            messages.success(request, 'Data saved successfully')
            return redirect('page5_edit', pk=request.session['household'])

    return render(request, 'page5.html',
                  {'production_and_sales_on_operational_holding_formset': croppingPattern_formset,
                   'production_and_sales_on_operational_holding_comment_form': croppingPatternCommentsForm
                   })


@login_required(login_url='login')
def edit(request, pk):
    try:
        request.session['household'] = pk  # TODO: temporary, remove when search functionality is implemented
        croppingPatternComments = get_object_or_404(CroppingPatternAndCropScheduleComments, household=pk)

        if request.method == "POST":
            croppingPattern_formset = formset_factory(CroppingPatternAndCropScheduleForm, formset=BaseFormSet, extra=5)

            croppingPatternForms = croppingPattern_formset(request.POST)
            croppingPatternCommentForm = CroppingPatternAndCropScheduleCommentsForm(request.POST,
                                                                                    instance=croppingPatternComments)
            crop_patterns_saved = False
            crop_patterns_comments_saved = False
            if croppingPatternForms.is_valid() and croppingPatternCommentForm.is_valid():
                CroppingPatternAndCropSchedule.objects.filter(household=pk).delete()
                CroppingPatternAndCropScheduleComments.objects.filter(household=pk).delete()
                crop_patterns_saved = save_forms(request, croppingPatternForms)
                crop_patterns_comments_saved = save_form_with_no_has_change(request, croppingPatternCommentForm)

            if crop_patterns_saved or crop_patterns_comments_saved:
                messages.success(request, 'Data saved successfully')

        croppingPattern_model_formset=modelformset_factory(CroppingPatternAndCropSchedule, form=CroppingPatternAndCropScheduleForm, extra=5)
        croppingPattern_result_set=CroppingPatternAndCropSchedule.objects.filter(household=pk)
        croppingPatternset=croppingPattern_model_formset(queryset=croppingPattern_result_set)

        croppingPatternCommentForms=CroppingPatternAndCropScheduleCommentsForm(instance=croppingPatternComments)

        return render(request, 'page5.html',
                      {'production_and_sales_on_operational_holding_formset': croppingPatternset,
                       'production_and_sales_on_operational_holding_comment_form': croppingPatternCommentForms
                        })
    except Exception:
        return new(request)


def get(household):
    try:
        croppingPattern = CroppingPatternAndCropSchedule.objects.get(household=household)
        croppingPatternComments = CroppingPatternAndCropScheduleComments.objects.get(household=household)

    except CroppingPatternAndCropSchedule.DoesNotExist and CroppingPatternAndCropScheduleComments.DoesNotExist:
        croppingPattern = None
        croppingPatternComments = None
    return croppingPattern, croppingPatternComments
