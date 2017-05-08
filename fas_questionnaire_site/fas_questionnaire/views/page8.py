from django.contrib import messages
from django.forms import modelformset_factory
from django.forms.formsets import formset_factory, BaseFormSet
from django.shortcuts import get_object_or_404, render, redirect

from .common import *
from ..forms.page8 import *
from ..models.page8 import *

@login_required(login_url='login')
def init(request):
    if request.session.get('household') is None:
        return redirect('household_edit')
    else:
        return edit(request, request.session['household'])


@login_required(login_url='login')
def edit(request, pk):
    request.session['household'] = pk
    if request.method == "POST":
        extension_formset = formset_factory(ExtensionForm, formset=BaseFormSet, extra=1)
        institutional_support_formset = formset_factory(InstitutionalSupportForm, formset=BaseFormSet, extra=1)

        extension_forms = extension_formset(request.POST, prefix='extensionforms')
        institutional_support_forms = institutional_support_formset(request.POST, prefix='institutionalsupportforms')

        if (save_formset(extension_forms, Extension, pk) and save_formset(institutional_support_forms, InstitutionalSupport, pk) and save_formset(get_comments_formset_to_save(request), Comments, pk, 8)):
            messages.success(request, "Data saved successfully")
            return redirect('page8_edit', pk)
        else:
            return render(request, 'page8.html', {'extension_formset': extension_forms,
                               'institutional_support_formset': institutional_support_forms,
                               'search_form': get_search_form(),
                                'comments': get_comments_formset(pk, 8)})

    extension_formset = modelformset_factory(Extension, form=ExtensionForm, extra=1)
    institutional_support_formset = modelformset_factory(InstitutionalSupport, form=InstitutionalSupportForm, extra=1)

    extension_result_set = Extension.objects.filter(household=pk)
    extensionformset = extension_formset(queryset=extension_result_set, prefix='extensionforms')

    institutional_support_result_set = InstitutionalSupport.objects.filter(household=pk)
    institutionalsupportformset = institutional_support_formset(queryset=institutional_support_result_set,
                                                                prefix='institutionalsupportforms')

    return render(request, 'page8.html', {'extension_formset': extensionformset,
                                            'institutional_support_formset': institutionalsupportformset,
                                            'search_form': get_search_form(),
                                            'comments': get_comments_formset(pk, 8)})