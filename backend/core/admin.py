from django.contrib import admin
from .models import Client, ClientHouseholdMember, ClientHouseholdBenefit, AvailableBenefit

# Register your models here.
admin.site.register(Client)
admin.site.register(ClientHouseholdMember)
admin.site.register(ClientHouseholdBenefit)
admin.site.register(AvailableBenefit)