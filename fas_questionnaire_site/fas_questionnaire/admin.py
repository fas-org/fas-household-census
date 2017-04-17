from django.contrib import admin
from .models.household_models import Household, Village
from .models.introduction_models_section1 import Sex
from .models.householdmembers import LiteracyStatus, CalendarGranularity
from .models.othercosts import OtherCostsItems
from .models.page_13 import WageUnit, TypeOfWage
from .models.common import Crop, PlaceOfWork


admin.site.register(OtherCostsItems)
admin.site.register(LiteracyStatus)
admin.site.register(CalendarGranularity)
admin.site.register(Village)
admin.site.register(Sex)
admin.site.register(Crop)
admin.site.register(PlaceOfWork)
admin.site.register(WageUnit)
admin.site.register(TypeOfWage)
