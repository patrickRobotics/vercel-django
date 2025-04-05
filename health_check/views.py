from django.http import JsonResponse

def health_check(request):
    data = {
        'app': 'zynastock ussd',
    }
    return JsonResponse(data)