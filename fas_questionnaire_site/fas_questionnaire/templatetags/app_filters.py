from django import template
from django.contrib.auth.models import Group
from ..models.household_models import Household
register = template.Library()


@register.filter(name='has_group')
def has_group(user, group_name):
    group = Group.objects.get(name=group_name)
    return group in user.groups.all()


@register.filter(name='is_submitted')
def is_submitted(household_id):
    household = Household.objects.get(pk=household_id)
    return household.is_submitted