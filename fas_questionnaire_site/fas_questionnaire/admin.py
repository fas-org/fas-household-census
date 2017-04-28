from django.contrib import admin
from .models.common import Sex, Crop, PlaceOfWork, Caste, LandType
from .models.household_models import Village
from .models.page1 import LiteracyStatus, MaritalStatus, CalendarGranularity, Relationship, Occupation, Education, Religion, TehsilOfBirth
from .models.page10 import OtherCostsItems
from .models.page_13 import WageUnit, TypeOfWage
from .models.page20 import SourceOfBorrowing, PurposeOfBorrowing, MonthWhenFullyRepaid, BankNgoToWhichTheGroupIsLinked, PeriodOfMembership, NameOfBankPostOffice, TypeOfAccount
from .models.page22 import InvestigationNeeded

#Common
admin.site.register(Sex)
admin.site.register(Crop)
admin.site.register(PlaceOfWork)
admin.site.register(Caste)
admin.site.register(LandType)

#household_models
admin.site.register(Village)

#Page 1
admin.site.register(CalendarGranularity)
admin.site.register(Relationship)
admin.site.register(LiteracyStatus)
admin.site.register(MaritalStatus)
admin.site.register(Occupation)
admin.site.register(Education)
admin.site.register(Religion)
admin.site.register(TehsilOfBirth)

#Page 10
admin.site.register(OtherCostsItems)

#Page 13
admin.site.register(WageUnit)
admin.site.register(TypeOfWage)

#Page 20
admin.site.register(SourceOfBorrowing)
admin.site.register(PurposeOfBorrowing)
admin.site.register(MonthWhenFullyRepaid)
admin.site.register(BankNgoToWhichTheGroupIsLinked)
admin.site.register(PeriodOfMembership)
admin.site.register(NameOfBankPostOffice)
admin.site.register(TypeOfAccount)

#Page 22
admin.site.register(InvestigationNeeded)