from django.db import models


class PatternOfAgriculturalLabouringOut(models.Model):
    id = models.AutoField(primary_key=True)
    name_of_worker = models.IntegerField(db_column='name_of_worker', blank=True, null=True)
    sex = models.ForeignKey('Sex', on_delete= models.CASCADE, blank=True, null=True)
    crop = models.ForeignKey('Crop', on_delete= models.CASCADE, blank=True, null=True)
    operation = models.CharField(max_length=50, blank=True, null=True)
    type_of_wage = models.ForeignKey('TypeOfWage', on_delete= models.CASCADE, blank=True, null=True)
    place_of_work = models.ForeignKey('PlaceOfWork', on_delete= models.CASCADE, blank=True, null=True)
    labour_days = models.FloatField(blank=True, null=True)
    wages_cash = models.FloatField(blank=True, null=True)
    wages_kind = models.CharField(max_length=100, blank=True, null=True)
    unit = models.ForeignKey('WageUnit', on_delete= models.CASCADE, blank=True, null=True)
    hours_of_work = models.FloatField(blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    household = models.ForeignKey('Household', on_delete= models.CASCADE, db_column='household')

    class Meta:
        managed = True
        db_table = 'pattern_of_agricultural_labouring_out'

    def __str__(self):
        return self.name_of_worker


class WageUnit(models.Model):
    unit = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'wage_unit'

    def __str__(self):
        return self.unit


class TypeOfWage(models.Model):
    type = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'type_of_wage'

    def __str__(self):
        return self.type

