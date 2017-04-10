from ..forms.source_and_type_of_extension_services_forms_section8 import ExtensionForm, InstitutionalSupportForm, \
    InstitutionalSupportCommentsForm
from ..models.source_and_type_of_extension_services_models_section8 import Extension, InstitutionalSupport, InstitutionalSupportComments
from django.shortcuts import get_object_or_404, render, redirect
from . import household as household
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.forms.formsets import formset_factory, BaseFormSet
from django.forms import modelformset_factory


@login_required(login_url='login')
def init(request):
    if request.session.get('household') is None:
        return new(request)
    else:
        extension_result_set = Extension.objects.filter(household=request.session.get('household'))
        initial_support_result_set = InstitutionalSupport.objects.filter(household=request.session.get('household'))
        initial_support_comments_result_set = InstitutionalSupportComments.objects.filter(household=request.session.get('household'))

        if len(extension_result_set) == 0 and len(initial_support_result_set) == 0 and len(initial_support_comments_result_set) == 0:
            return new(request)
        return edit(request, request.session['household'])


@login_required(login_url='login')
def new(request):
    extension_formset = formset_factory(ExtensionForm, formset=BaseFormSet, extra=5)
    institutional_support_formset = formset_factory(InstitutionalSupportForm, formset=BaseFormSet, extra=5)
    institutional_support_comments_form = InstitutionalSupportCommentsForm()
    if request.method == "POST":
        extensionforms = extension_formset(request.POST)
        institutionalsupportforms = institutional_support_formset(request.POST)
        institutional_support_comments_form = InstitutionalSupportCommentsForm(request.POST)

        form_saved = False
        if extensionforms.is_valid() and institutionalsupportforms.is_valid() and institutional_support_comments_form.is_valid():

            for extension_form in extensionforms:
                if extension_form.is_valid() and extension_form.has_changed():
                    cultivation_adviser = extension_form.save(commit=False)
                    cultivation_adviser.household = household.get(request.session['household'])
                    cultivation_adviser.save()

            for institutional_support_form in institutionalsupportforms:
                if institutional_support_form.is_valid() and institutional_support_form.has_changed():
                    institutional_support = institutional_support_form.save(commit=False)
                    institutional_support.household = household.get(request.session['household'])
                    institutional_support.save()

            if institutional_support_comments_form.is_valid() and institutional_support_comments_form.has_changed():
                institutional_support_comments = institutional_support_comments_form.save(commit=False)
                institutional_support_comments.household = household.get(request.session['household'])
                institutional_support_comments.save()
            form_saved = True

        if form_saved:
            messages.success(request, 'Data saved successfully')
            return redirect('extension_edit', pk=request.session['household'])

    return render(request, 'source_and_type_of_extension_services_section8.html',
                  {'extension_formset': extension_formset, 'institutional_support_formset': institutional_support_formset,
                   'institutional_support_comments_form': institutional_support_comments_form})


@login_required(login_url='login')
def edit(request, pk):
    try:
        institutional_support_comments = get_object_or_404(InstitutionalSupportComments, household=pk)

        if request.method == "POST":
            extension_formset = formset_factory(ExtensionForm, formset=BaseFormSet, extra=5)
            institutional_support_formset = formset_factory(InstitutionalSupportForm, formset=BaseFormSet, extra=5)

            extension_forms = extension_formset(request.POST)
            institutional_support_forms = institutional_support_formset(request.POST)
            institutional_support_comments_form = InstitutionalSupportCommentsForm(request.POST, instance=institutional_support_comments)

            Extension.objects.filter(household=pk).delete()
            InstitutionalSupport.objects.filter(household=pk).delete()
            InstitutionalSupportComments.objects.filter(household=pk).delete()

            form_saved = False

            if extension_forms.is_valid() and institutional_support_forms.is_valid() and institutional_support_comments_form.is_valid():
                for extension_form in extension_forms:
                    if extension_form.is_valid() and extension_form.has_changed():
                        cultivation_adviser = extension_form.save(commit=False)
                        cultivation_adviser.save()

                for institutional_support_form in institutional_support_forms:
                    if institutional_support_form.is_valid() and institutional_support_form.has_changed():
                        institutional_support = institutional_support_form.save(commit=False)
                        institutional_support.save()

                if institutional_support_comments_form.is_valid() and institutional_support_comments_form.has_changed():
                    institutional_support_comments = institutional_support_comments_form.save(commit=False)
                    institutional_support_comments.save()
                form_saved = True

            if form_saved:
                messages.success(request, 'Data saved successfully')
                return redirect('extension_edit', pk=pk)

        extension_formset = modelformset_factory(Extension, form=ExtensionForm, extra=5)
        institutional_support_formset = modelformset_factory(InstitutionalSupport, form=InstitutionalSupportForm, extra=5)

        extension_result_set = Extension.objects.filter(household=pk)
        extensionformset = extension_formset(queryset=extension_result_set)

        institutional_support_result_set = InstitutionalSupport.objects.filter(household=pk)
        institutionalsupportformset = institutional_support_formset(queryset=institutional_support_result_set)

        institutional_support_comments_form = InstitutionalSupportCommentsForm(instance=institutional_support_comments)
        return render(request, 'source_and_type_of_extension_services_section8.html',
                      {'extension_formset': extensionformset, 'institutional_support_formset': institutionalsupportformset,
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

    return extension, institutional_support, institutional_support_comments
