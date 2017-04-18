from django.contrib import admin
from .models.household_models import Household, Village
from .models.page1 import LiteracyStatus, MaritalStatus, CalendarGranularity
from .models.othercosts import OtherCostsItems
from .models.page_13 import WageUnit, TypeOfWage
from .models.common import Sex, Crop, PlaceOfWork, LandType


admin.site.register(OtherCostsItems)
admin.site.register(LiteracyStatus)
admin.site.register(MaritalStatus)
admin.site.register(CalendarGranularity)
admin.site.register(Village)
admin.site.register(Sex)
admin.site.register(Crop)
admin.site.register(PlaceOfWork)
admin.site.register(WageUnit)
admin.site.register(TypeOfWage)
admin.site.register(LandType)
