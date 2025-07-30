from datetime import date
from django.db import models

class Client(models.Model):
    class Meta:
        db_table = "client"

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    door_number = models.CharField(max_length=20)
    address_line_1 = models.CharField(max_length=50)
    address_line_2 = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=30)
    county = models.CharField(max_length=30)
    post_code = models.CharField(max_length=10)
    telephone_number = models.CharField(max_length=15, blank=True)
    date_of_birth: date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class ClientHouseholdMembers(models.Model):
    class Meta:
        db_table = "client_household_members"

    client_id: int = models.ForeignKey("Client", on_delete=models.CASCADE)
    num_adults: int = models.IntegerField(default=0)
    num_pensioners: int = models.IntegerField(default=0)
    num_children_0_to_5: int = models.IntegerField(default=0)
    num_children_6_to_11: int = models.IntegerField(default=0)
    num_children_12_to_17: int = models.IntegerField(default=0)


class ClientHouseholdBenefits(models.Model):
    class Meta:
        db_table = "client_household_benefits"

    client_id: int = models.ForeignKey("Client", on_delete=models.CASCADE)
    benefit_type: int = models.IntegerField(null=True)


class AvailableBenefits(models.Model):
    class Meta:
        db_table = "available_benefits"

    name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}"