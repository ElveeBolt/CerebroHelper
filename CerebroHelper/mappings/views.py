from django.conf import settings
from .services import services
from django.shortcuts import render


# Create your views here.
def mappings(request):
    context = {
        'title': 'Генерация Mappings',
        'mappings': settings.MAPPINGS
    }

    if request.method == 'POST':
        mappings = services.generate_mappings(request.POST.getlist('mappings'))
        services.save_json(mappings)
        context['download'] = settings.MEDIA_URL + settings.GENERATED_MAPPINGS

    return render(request, 'mappings/index.html', context=context)