from django.contrib import admin
from .models.household_models import Household, Village
from .models.page1 import Sex, LiteracyStatus, MaritalStatus, CalendarGranularity
from .models.page10 import OtherCostsItems
from .models.page_13 import WageUnit, TypeOfWage
from .models.common import Crop, PlaceOfWork, Caste


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
admin.site.register(Caste)
