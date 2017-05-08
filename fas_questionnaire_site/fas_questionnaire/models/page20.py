# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals
from django.db import models
from .household_models import Household


class SourceOfBorrowing(models.Model):
    id = models.AutoField(primary_key=True)
    source_of_borrowing = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'source of borrowing'

    def __str__(self):
        return self.source_of_borrowing

class PurposeOfBorrowing(models.Model):
    id = models.AutoField(primary_key=True)
    purpose_of_borrowing = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'purpose of borrowing'

    def __str__(self):
        return self.purpose_of_borrowing

class OutstandingLoans(models.Model):
    id = models.AutoField(primary_key=True)
    household = models.ForeignKey(Household, models.DO_NOTHING,db_column='household')
    loan_no = models.IntegerField(db_column='loan no', blank=True, null=True)
    month_and_year_of_borrowing = models.CharField(db_column='month and year of borrowing', max_length=50, blank=True, null=True)
    principal = models.CharField(db_column='principal', max_length=50, blank=True, null=True)
    collateral = models.CharField(db_column='collateral', max_length=50, blank=True, null=True)
    rate_of_interest = models.CharField(db_column='rate of interest', max_length=50, blank=True, null=True)
    principal_amount_outstanding = models.CharField(db_column='principal amount outstanding', max_length=50, blank=True, null=True)
    interest_amount_outstanding = models.CharField(db_column='interest amount outstanding', max_length=50, blank=True, null=True)
    total_amount_outstanding = models.CharField(db_column='total amount outstanding', max_length=50, blank=True, null=True)
    amount_repaid = models.CharField(db_column='amount repaid', max_length=50, blank=True, null=True)
    source_of_borrowing = models.ForeignKey(SourceOfBorrowing, models.DO_NOTHING, db_column='source of borrowing', blank=True, null=True)
    purpose_of_borrowing = models.ForeignKey(PurposeOfBorrowing, models.DO_NOTHING, db_column='purpose of borrowing', blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Outstanding loans'

class LoansBorrowedLastYearAndRepaid(models.Model):
    id = models.AutoField(primary_key=True)
    household = models.ForeignKey(Household, models.DO_NOTHING,db_column='household')
    loan_no = models.IntegerField(db_column='loan no', blank=True, null=True)
    month_of_borrowing = models.CharField(db_column='month of borrowing', max_length=100, blank=True, null=True)
    principal = models.CharField(db_column='principal', max_length=50, blank=True, null=True)
    collateral = models.CharField(db_column='collateral', max_length=50, blank=True, null=True)
    rate_of_interest = models.CharField(db_column='rate of interest', max_length=50, blank=True, null=True)
    month_when_fully_repaid = models.ForeignKey('Month', models.DO_NOTHING, db_column='Month When Fully Repaid', blank=True, null=True)
    total_amount_repaid = models.CharField(db_column='total amount repaid', max_length=50, blank=True, null=True)
    source_of_borrowing = models.ForeignKey(SourceOfBorrowing, models.DO_NOTHING, db_column='source of borrowing', blank=True, null=True)
    purpose_of_borrowing = models.ForeignKey(PurposeOfBorrowing, models.DO_NOTHING, db_column='purpose of borrowing', blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Loans borrowed last year and repaid'

class BankNgoToWhichTheGroupIsLinked(models.Model):
    id = models.AutoField(primary_key=True)
    bank_ngo_to_which_the_group_is_linked = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'bank_ngo_to_which_the_group_is_linked'

    def __str__(self):
        return self.bank_ngo_to_which_the_group_is_linked

class PeriodOfMembership(models.Model):
    id = models.AutoField(primary_key=True)
    period_of_membership = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'period_of_membership'

    def __str__(self):
        return self.period_of_membership

class MembershipInSelfHelpGroups(models.Model):
    id = models.AutoField(primary_key=True)
    household = models.ForeignKey(Household, models.DO_NOTHING,db_column='household')
    name_of_member = models.ForeignKey('HouseholdMembers', db_column='name of member', max_length=100, blank=True, null=True)
    name_of_group_group_leader = models.CharField(db_column='name of group group leader', max_length=100, blank=True, null=True)
    bank_ngo_to_which_the_group_is_linked = models.ForeignKey(BankNgoToWhichTheGroupIsLinked, models.DO_NOTHING, db_column='Bank Ngo To Which The Group is Linked', blank=True, null=True)
    period_of_membership = models.ForeignKey(PeriodOfMembership, models.DO_NOTHING, db_column='Period Of Membership', blank=True, null=True)
    number_of_members_in_the_group = models.IntegerField(db_column='number of members in the group', blank=True, null=True)
    rs_per_week_month_savings = models.IntegerField(db_column='rs per week month savings', blank=True, null=True)
    total_savings = models.IntegerField(db_column='total savings', blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Membership in self help groups'

class NameOfBankPostOffice(models.Model):
    id = models.AutoField(primary_key=True)
    name_of_bank_post_office = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'name_of_bank_post_office'

    def __str__(self):
        return self.name_of_bank_post_office

class TypeOfAccount(models.Model):
    id = models.AutoField(primary_key=True)
    type_of_account = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'type_of_account'

    def __str__(self):
        return self.type_of_account

class DetailsOfBankPostofficeAccountOfTheHousehold(models.Model):
    id = models.AutoField(primary_key=True)
    household = models.ForeignKey(Household, models.DO_NOTHING,db_column='household')
    name_of_account_holder = models.ForeignKey('HouseholdMembers', db_column='name of account holder', max_length=100, blank=True, null=True)
    name_of_bank_post_office = models.ForeignKey(NameOfBankPostOffice, models.DO_NOTHING, db_column='Name Of Bank Post Office', blank=True, null=True)
    type_of_account = models.ForeignKey(TypeOfAccount, models.DO_NOTHING, db_column='Type Of Account', blank=True, null=True)
    date_of_last_transaction = models.CharField(db_column='date of last transaction', max_length=100, blank=True, null=True)
    current_balanace = models.IntegerField(db_column='current balanace', blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'DetailsOfBankPostofficeAccountOfTheHousehold'
