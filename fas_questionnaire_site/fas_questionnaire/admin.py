from django.contrib import admin
from .models.household_models import Household, Village
from .models.introduction_models_section1 import Sex
from .models.householdmembers import LiteracyStatus, CalendarGranularity
from .models.othercosts import OtherCostsItems


admin.site.register(OtherCostsItems)
admin.site.register(LiteracyStatus)
admin.site.register(CalendarGranularity)
admin.site.register(Village)
admin.site.register(Sex)