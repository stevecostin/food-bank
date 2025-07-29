from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/global-configuration/', views.get_global_configuration, name='get_global_configuration'),
]