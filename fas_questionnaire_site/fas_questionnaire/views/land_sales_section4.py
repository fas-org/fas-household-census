from ..forms.land_sales_forms_section4 import LandSoldForm, LandPurchasedForm, LandPurchasedCommentsForm
from ..models.land_sales_models_section4 import LandSold, LandPurchased, LandPurchasedComments
from django.shortcuts import get_object_or_404, render, redirect
from . import household as household
from django.contrib.auth.decorators import login_required
from django.forms.formsets import formset_factory, BaseFormSet
from django.contrib import messages
from django.forms import modelformset_factory


@login_required(login_url='login')
def init(request):
    if request.session.get('household') is None:
        return new(request)
    else:
        landsold_result_set = LandSold.objects.filter(household=request.session.get('household'))
        landpurchased_result_set = LandPurchased.objects.filter(household=request.session.get('household'))

        if len(landsold_result_set) == 0 and len(landpurchased_result_set) == 0:
            return new(request)
        return edit(request, request.session['household'])


@login_required(login_url='login')
def new(request):
    landsold_formset = formset_factory(LandSoldForm, formset=BaseFormSet, extra=5)
    landpurchased_formset = formset_factory(LandPurchasedForm, formset=BaseFormSet, extra=5)
    landpurchased_comments_form = LandPurchasedCommentsForm()
    if request.method == "POST":
        landsoldforms = landsold_formset(request.POST)
        landpurchasedforms = landpurchased_formset(request.POST)
        landpurchased_comments_form = LandPurchasedCommentsForm(request.POST)

        form_saved = False
        if landsoldforms.is_valid() and landpurchasedforms.is_valid() and landpurchased_comments_form.is_valid():
            for landsoldform in landsoldforms:
                if landsoldform.is_valid() and landsoldform.has_changed():
                    landsold = landsoldform.save(commit=False)
                    landsold.household = household.get(request.session['household'])
                    landsold.save()
                    form_saved = True

            for landpurchasedform in landpurchasedforms:
                if landpurchasedform.is_valid() and landpurchasedform.has_changed():
                    landpurchased = landpurchasedform.save(commit=False)
                    landpurchased.household = household.get(request.session['household'])
                    landpurchased.save()
                    form_saved = True

            if landpurchased_comments_form.is_valid() and landpurchased_comments_form.has_changed():
                landpurchased_comments = landpurchased_comments_form.save(commit=False)
                landpurchased_comments.household = household.get(request.session['household'])
                landpurchased_comments.save()
                form_saved = True

        if form_saved:
            messages.success(request, 'Data saved successfully')
            return redirect('landsales_edit', pk=request.session['household'])

    return render(request, 'land_sales_section4.html', {'landsold_formset': landsold_formset,
                                                        'landpurchased_formset': landpurchased_formset,
                                                        'landpurchased_comments_form': landpurchased_comments_form})


@login_required(login_url='login')
def edit(request, pk):
    try:
        landpurchased_comments = get_object_or_404(LandPurchasedComments, household=pk)
        if request.method == "POST":
            landsold_formset = formset_factory(LandSoldForm, formset=BaseFormSet, extra=5)
            landpurchased_formset = formset_factory(LandPurchasedForm, formset=BaseFormSet, extra=5)

            landsoldforms = landsold_formset(request.POST)
            landpurchasedforms = landpurchased_formset(request.POST)
            landpurchased_comments_form = LandPurchasedCommentsForm(request.POST, instance=landpurchased_comments)

            LandSold.objects.filter(household=pk).delete()
            LandPurchased.objects.filter(household=pk).delete()
            # LandPurchasedComments.objects.filter(household=pk).delete()

            form_saved = False
            if landsoldforms.is_valid() and landpurchasedforms.is_valid() and landpurchased_comments_form.is_valid():
                for landsoldform in landsoldforms:
                    if landsoldform.is_valid() and landsoldform.has_changed():
                        landsold = landsoldform.save(commit=False)
                        landsold.household = household.get(request.session['household'])
                        landsold.save()
                        form_saved = True

                for landpurchasedform in landpurchasedforms:
                    if landpurchasedform.is_valid() and landpurchasedform.has_changed():
                        landpurchased = landpurchasedform.save(commit=False)
                        landpurchased.household = household.get(request.session['household'])
                        landpurchased.save()
                        form_saved = True

                if landpurchased_comments_form.is_valid() and landpurchased_comments_form.has_changed():
                    landpurchased_comments = landpurchased_comments_form.save(commit=False)
                    landpurchased_comments.save()
                    form_saved = True

            if form_saved:
                messages.success(request, 'Data saved successfully')
                return redirect('landsales_edit', pk=request.session['household'])

        landsold_formset = modelformset_factory(LandSold, form=LandSoldForm, extra=5)
        landpurchased_formset = modelformset_factory(LandPurchased, form=LandPurchasedForm, extra=5)

        landsold_result_set = LandSold.objects.filter(household=pk)
        landsoldformset = landsold_formset(queryset=landsold_result_set)

        landpurchased_result_set = LandPurchased.objects.filter(household=pk)
        landpurchasedformset = landpurchased_formset(queryset=landpurchased_result_set)

        landpurchased_comments_form = LandPurchasedCommentsForm(instance=landpurchased_comments)

        return render(request, 'land_sales_section4.html',
                      {'landsold_formset': landsoldformset, 'landpurchased_formset': landpurchasedformset,
                       'landpurchased_comments_form': landpurchased_comments_form})
    except Exception:
        return new(request)


@login_required(login_url='login')
def get(household):
    try:
        landsold = LandSold.objects.get(household=household)
        landpurchased = LandPurchased.objects.get(household=household)
    except LandSold.DoesNotExist and LandPurchased.DoesNotExist:
        landsold = None
        landpurchased = None
    return landsold, landpurchased
