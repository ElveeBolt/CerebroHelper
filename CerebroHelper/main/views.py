from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title': 'Главная страница'
    }
    return render(request, 'main/index.html', context=context)