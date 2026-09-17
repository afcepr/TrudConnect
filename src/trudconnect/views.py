from django.shortcuts import render
import datetime


def index(request):
    date = datetime.datetime.now().date()
    title = 'TrudConnect'
    _context = {'date': date, 'title': title}
    return render(request, 'index.html', context=_context)
