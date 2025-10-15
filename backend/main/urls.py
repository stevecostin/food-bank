from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

urlpatterns = [
    # Admin portal
    path('admin/', admin.site.urls),

    path('api-auth/', include('rest_framework.urls')),

    # Accounts
    path('accounts/', include('accounts.urls')),

    # Global configuration
    path('global/', include('global_site.urls')),

    # Frontend API's
    path('api/', include('frontend_api.urls')),

    # Core
    path('core/', include('core.urls')),
]

# urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]