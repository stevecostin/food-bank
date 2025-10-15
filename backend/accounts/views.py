from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from django.contrib import auth
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect

@method_decorator(csrf_protect, name='dispatch')
class CheckAuthenticatedView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        try:
            is_authenticated = request.user.is_authenticated

            if is_authenticated:
                return Response({'is_authenticated': 'success'})
            else:
                return Response({'is_authenticated': 'error'})
        except:
            return Response({'error': 'Something went wrong when checking the authentication status'})


@method_decorator(csrf_protect, name='dispatch')
class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        try:
            data = self.request.data

            email = data['email']
            password = data['password']

            user = auth.authenticate(email=email, password=password)

            if user is not None:
                auth.login(request, user)

                return Response({'success': 'User authenticated', 'email': email})
            else:
                return Response({'error': 'Error authenticating'})
        except:
            return Response({'error': 'Something went wrong when logging in'})


class LogoutView(APIView):
    def post(self, request, format=None):
        try:
            auth.logout(request)

            return Response({'success': 'Logged out'})
        except:
            return Response({'error': 'Something went wrong when logging out'})


@method_decorator(ensure_csrf_cookie, name='dispatch')
class GetCSRFToken(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        return Response({'success': 'CSRF cookie set'})
