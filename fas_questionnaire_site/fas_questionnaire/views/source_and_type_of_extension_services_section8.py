from ..forms.source_and_type_of_extension_services_forms_section8 import ExtensionForm, InstitutionalSupportForm, InstitutionalSupportCommentsForm
from ..models.source_and_type_of_extension_services_models_section8 import Extension, InstitutionalSupport, InstitutionalSupportComments
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
        extension_form = ExtensionForm(request.POST)
        institutional_support_form = InstitutionalSupportForm(request.POST)
        institutional_support_comments_form = InstitutionalSupportCommentsForm(request.POST)

        if extension_form.is_valid() and institutional_support_form.is_valid() and institutional_support_comments_form.is_valid():
            cultivation_adviser = extension_form.save(commit=False)
            cultivation_adviser.household = household.get(request.session['household'])
            cultivation_adviser.save()

            institutional_support = institutional_support_form.save(commit=False)
            institutional_support.household = household.get(request.session['household'])
            institutional_support.save()

            institutional_support_comments = institutional_support_comments_form.save(commit=False)
            institutional_support_comments.household = household.get(request.session['household'])
            institutional_support_comments.save()

            messages.success(request, 'Data saved successfully')
            return redirect('extension_edit', pk=request.session['household'])
    else:
        extension_form = ExtensionForm()
        institutional_support_form = InstitutionalSupportForm()
        institutional_support_comments_form = InstitutionalSupportCommentsForm()

    return render(request, 'source_and_type_of_extension_services_section8.html',
                  {'extension_form': extension_form, 'institutional_support_form': institutional_support_form,
                   'institutional_support_comments_form': institutional_support_comments_form})


@login_required(login_url='login')
def edit(request, pk):
    try:
        extension = get_object_or_404(Extension, household=pk)
        institutional_support = get_object_or_404(InstitutionalSupport, household=pk)
        institutional_support_comments = get_object_or_404(InstitutionalSupportComments, household=pk)

        if request.method == "POST":
            extension_form = ExtensionForm(request.POST, instance=extension)
            institutional_support_form = InstitutionalSupportForm(request.POST, instance=institutional_support)
            institutional_support_comments_form = InstitutionalSupportCommentsForm(request.POST, instance=institutional_support_comments)

            if extension_form.is_valid() and institutional_support_form.is_valid():
                cultivation_adviser = extension_form.save(commit=False)
                cultivation_adviser.save()

                institutional_support = institutional_support_form.save(commit=False)
                institutional_support.save()

                institutional_support_comments = institutional_support_comments_form.save(commit=False)
                institutional_support_comments.save()

                messages.success(request, 'Data saved successfully')

                return redirect('extension_edit', pk=pk)
        else:
            extension_form = ExtensionForm(instance=extension)
            institutional_support_form = InstitutionalSupportForm(instance=institutional_support)
            institutional_support_comments_form = InstitutionalSupportCommentsForm(instance=institutional_support_comments)

        return render(request, 'source_and_type_of_extension_services_section8.html',
                      {'extension_form': extension_form, 'institutional_support_form': institutional_support_form,
                       'institutional_support_comments_form': institutional_support_comments_form})
    except Exception:
        return new(request)


@login_required(login_url='login')
def get(household):
    try:
        extension = Extension.objects.get(household=household)
        institutional_support = InstitutionalSupport.objects.get(household=household)
        institutional_support_comments = InstitutionalSupportComments.objects.get(household=household)

    except Exception.DoesNotExist:
        extension = None
        institutional_support = None
        institutional_support_comments = None

    return extension, institutional_support,institutional_support_comments
