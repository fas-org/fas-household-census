from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Household
from ..forms import HouseholdForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class HouseholdListView(ListView):
    model = Household
    template_name = "household_info/household_list.html"
    paginate_by = 20
    context_object_name = "household_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(HouseholdListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(HouseholdListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(HouseholdListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(HouseholdListView, self).get_queryset()

    def get_allow_empty(self):
        return super(HouseholdListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(HouseholdListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(HouseholdListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(HouseholdListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(HouseholdListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(HouseholdListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(HouseholdListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(HouseholdListView, self).get_template_names()


class HouseholdDetailView(DetailView):
    model = Household
    template_name = "household_info/household_detail.html"
    context_object_name = "household"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(HouseholdDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(HouseholdDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(HouseholdDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(HouseholdDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(HouseholdDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(HouseholdDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(HouseholdDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(HouseholdDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(HouseholdDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(HouseholdDetailView, self).get_template_names()


class HouseholdCreateView(CreateView):
    model = Household
    form_class = HouseholdForm
    template_name = "household_info/household_create.html"
    success_url = reverse_lazy("household_list")

    def __init__(self, **kwargs):
        return super(HouseholdCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(HouseholdCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(HouseholdCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(HouseholdCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(HouseholdCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(HouseholdCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(HouseholdCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(HouseholdCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(HouseholdCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(HouseholdCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(HouseholdCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(HouseholdCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(HouseholdCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("household_detail", args=(self.object.pk,))


class HouseholdUpdateView(UpdateView):
    model = Household
    form_class = HouseholdForm
    template_name = "household_info/household_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "household"

    def __init__(self, **kwargs):
        return super(HouseholdUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(HouseholdUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(HouseholdUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(HouseholdUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(HouseholdUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(HouseholdUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(HouseholdUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(HouseholdUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(HouseholdUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(HouseholdUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(HouseholdUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(HouseholdUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(HouseholdUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(HouseholdUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(HouseholdUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(HouseholdUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(HouseholdUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("household_detail", args=(self.object.pk,))


class HouseholdDeleteView(DeleteView):
    model = Household
    template_name = "household_info/household_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "household"

    def __init__(self, **kwargs):
        return super(HouseholdDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(HouseholdDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(HouseholdDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(HouseholdDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(HouseholdDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(HouseholdDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(HouseholdDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(HouseholdDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(HouseholdDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(HouseholdDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(HouseholdDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("household_list")
