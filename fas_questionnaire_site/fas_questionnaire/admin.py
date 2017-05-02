from django.contrib import admin
from fas_questionnaire.models.page2 import AcquisitionMode, IrrigationSource, IrrigationFlow, IrrigationOwnership, \
    HomesteadComponents
from fas_questionnaire.models.page3 import Registration, TypeOfContract
from fas_questionnaire.models.page4 import InterestUsufruct, SeasonalYearlyOther
from fas_questionnaire.models.page5 import Tenurial, HomesteadLand
from fas_questionnaire.models.page6 import WhereMarketed, MarketingAgencies, ModeOfTransport
from .models.household_models import Village
from .models.page10 import OtherCostsItems
from .models.page_13 import WageUnit, TypeOfWage
from .models.page19 import TypeOfRationCard, ColorOfCard, SourceOfWater, SourceOfWaterOwnership, WaterSourceDistanceFromHouse, PurposeForWhichUsed, WhetherOwnedOrRented,TypeOfRoof,TypeOfWall,TypeOfFloor,Latrine,ElectricityConnection,SourceOfEnergyForCooking,NatureOfDisbursement
from .models.page1 import *
from .models.page18 import DescriptionOfAssets
from .models.common import Sex, Crop, PlaceOfWork, Caste, LandType, Units, Month, YesOrNo
from .models.page20 import SourceOfBorrowing, PurposeOfBorrowing, BankNgoToWhichTheGroupIsLinked, PeriodOfMembership, NameOfBankPostOffice, TypeOfAccount

#Common
admin.site.register(Sex)
admin.site.register(Crop)
admin.site.register(PlaceOfWork)
admin.site.register(Caste)
admin.site.register(LandType)
admin.site.register(Registration)
admin.site.register(YesOrNo)
admin.site.register(Month)

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

#page2
admin.site.register(AcquisitionMode)
admin.site.register(IrrigationSource)
admin.site.register(IrrigationFlow)
admin.site.register(IrrigationOwnership)
admin.site.register(HomesteadComponents)

#page3
admin.site.register(Units)
admin.site.register(TypeOfContract)


#page4
admin.site.register(InterestUsufruct)
admin.site.register(SeasonalYearlyOther)

#page5
admin.site.register(Tenurial)
admin.site.register(HomesteadLand)

#page6
admin.site.register(WhereMarketed)
admin.site.register(MarketingAgencies)
admin.site.register(ModeOfTransport)

#Page 10
admin.site.register(OtherCostsItems)

#Page 13
admin.site.register(WageUnit)
admin.site.register(TypeOfWage)

#page18
admin.site.register(DescriptionOfAssets)

#Page 19
admin.site.register(TypeOfRationCard)
admin.site.register(ColorOfCard)
admin.site.register(SourceOfWater)
admin.site.register(SourceOfWaterOwnership)
admin.site.register(WaterSourceDistanceFromHouse)
admin.site.register(PurposeForWhichUsed)
admin.site.register(WhetherOwnedOrRented)
admin.site.register(TypeOfRoof)
admin.site.register(TypeOfWall)
admin.site.register(TypeOfFloor)
admin.site.register(SourceOfEnergyForCooking)
admin.site.register(Latrine)
admin.site.register(NatureOfDisbursement)

#Page 20
admin.site.register(SourceOfBorrowing)
admin.site.register(PurposeOfBorrowing)
admin.site.register(BankNgoToWhichTheGroupIsLinked)
admin.site.register(PeriodOfMembership)
admin.site.register(NameOfBankPostOffice)
admin.site.register(TypeOfAccount)