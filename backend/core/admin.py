from django.contrib import admin
from .models import Client, ClientHouseholdMembers, ClientHouseholdBenefits, AvailableBenefits

# Register your models here.
admin.site.register(Client)
admin.site.register(ClientHouseholdMembers)
admin.site.register(ClientHouseholdBenefits)
admin.site.register(AvailableBenefits)