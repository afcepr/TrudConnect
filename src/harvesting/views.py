from django.shortcuts import render
from .models import Vacancy


def index_view(request):
    qs = Vacancy.objects.all()
    return render(request, 'harvesting/index.html', {'object_list': qs})
