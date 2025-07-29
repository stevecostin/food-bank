from django.http.response import JsonResponse
from .models import GlobalConfiguration

def get_global_configuration(request):
    global_config = GlobalConfiguration()

    return JsonResponse({
        'site-name': global_config.name
    })