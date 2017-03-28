from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import HouseholdMembers
from ..forms import HouseholdMembersForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class HouseholdMembersListView(ListView):
    model = HouseholdMembers
    template_name = "household_info/household_members_list.html"
    paginate_by = 20
    context_object_name = "household_members_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(HouseholdMembersListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(HouseholdMembersListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(HouseholdMembersListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(HouseholdMembersListView, self).get_queryset()

    def get_allow_empty(self):
        return super(HouseholdMembersListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(HouseholdMembersListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(HouseholdMembersListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(HouseholdMembersListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(HouseholdMembersListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(HouseholdMembersListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(HouseholdMembersListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(HouseholdMembersListView, self).get_template_names()


class HouseholdMembersDetailView(DetailView):
    model = HouseholdMembers
    template_name = "household_info/household_members_detail.html"
    context_object_name = "household_members"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(HouseholdMembersDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(HouseholdMembersDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(HouseholdMembersDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(HouseholdMembersDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(HouseholdMembersDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(HouseholdMembersDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(HouseholdMembersDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(HouseholdMembersDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(HouseholdMembersDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(HouseholdMembersDetailView, self).get_template_names()


class HouseholdMembersCreateView(CreateView):
    model = HouseholdMembers
    form_class = HouseholdMembersForm
    template_name = "household_info/household_members_create.html"
    success_url = reverse_lazy("household_members_list")

    def __init__(self, **kwargs):
        return super(HouseholdMembersCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(HouseholdMembersCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(HouseholdMembersCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(HouseholdMembersCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(HouseholdMembersCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(HouseholdMembersCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(HouseholdMembersCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(HouseholdMembersCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(HouseholdMembersCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(HouseholdMembersCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(HouseholdMembersCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(HouseholdMembersCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(HouseholdMembersCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("household_members_detail", args=(self.object.pk,))


class HouseholdMembersUpdateView(UpdateView):
    model = HouseholdMembers
    form_class = HouseholdMembersForm
    template_name = "household_info/household_members_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "household_members"

    def __init__(self, **kwargs):
        return super(HouseholdMembersUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(HouseholdMembersUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(HouseholdMembersUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(HouseholdMembersUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(HouseholdMembersUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(HouseholdMembersUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(HouseholdMembersUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(HouseholdMembersUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(HouseholdMembersUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(HouseholdMembersUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(HouseholdMembersUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(HouseholdMembersUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(HouseholdMembersUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(HouseholdMembersUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(HouseholdMembersUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(HouseholdMembersUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(HouseholdMembersUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("household_members_detail", args=(self.object.pk,))


class HouseholdMembersDeleteView(DeleteView):
    model = HouseholdMembers
    template_name = "household_info/household_members_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "household_members"

    def __init__(self, **kwargs):
        return super(HouseholdMembersDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(HouseholdMembersDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(HouseholdMembersDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(HouseholdMembersDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(HouseholdMembersDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(HouseholdMembersDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(HouseholdMembersDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(HouseholdMembersDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(HouseholdMembersDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(HouseholdMembersDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(HouseholdMembersDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("household_members_list")
