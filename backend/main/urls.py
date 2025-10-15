from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin portal
    path('admin/', admin.site.urls),

    # Global configuration
    path('', include('global_site.urls')),

    # Frontend API's
    path('', include('frontend_api.urls')),

    # Core
    path('', include('core.urls')),
]
