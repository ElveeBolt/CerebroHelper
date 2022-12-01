from django.conf import settings
from .services import services
from django.shortcuts import render


# Create your views here.
def config(request):
    context = {
        'title': 'Генерация Config'
    }

    if request.method == 'POST':
        data = {
            'database': request.POST.getlist('database')[0]
        }
        services.save_json(data)
        context['download'] = settings.MEDIA_URL + settings.GENERETED_CONFIG

    return render(request, 'config/index.html', context=context)