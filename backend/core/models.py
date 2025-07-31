from datetime import date
from django.db import models
from django.db.models import CompositePrimaryKey


class Client(models.Model):
    class Meta:
        db_table = "client"

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    door_number = models.CharField(max_length=20)
    address_line_1 = models.CharField(max_length=50)
    address_line_2 = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=30)
    county = models.CharField(max_length=30)
    post_code = models.CharField(max_length=10)
    telephone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class ClientHouseholdMembers(models.Model):
    class Meta:
        db_table = "client_household_members"

    client = models.ForeignKey("Client", on_delete=models.CASCADE)
    num_adults = models.IntegerField(default=0)
    num_pensioners = models.IntegerField(default=0)
    num_children_0_to_5 = models.IntegerField(default=0)
    num_children_6_to_11 = models.IntegerField(default=0)
    num_children_12_to_17 = models.IntegerField(default=0)


class ClientHouseholdBenefits(models.Model):
    class Meta:
        db_table = "client_household_benefits"

    pk = CompositePrimaryKey("client_id", "benefit_type_id")
    client = models.ForeignKey("Client", on_delete=models.CASCADE)
    benefit_type = models.ForeignKey("AvailableBenefits", on_delete=models.CASCADE)


class AvailableBenefits(models.Model):
    class Meta:
        db_table = "available_benefits"

    name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}"