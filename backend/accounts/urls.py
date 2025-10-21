from django.urls import path
from .views import GetCSRFToken, LoginView, LogoutView, CheckAuthenticatedView

urlpatterns = [
    path('csrf_token', GetCSRFToken.as_view()),
    path('login', LoginView.as_view()),
    path('logout', LogoutView.as_view()),
    path('authenticated', CheckAuthenticatedView.as_view())
]