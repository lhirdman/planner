from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from weekly.models import Event, StdEvent
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime

def index(request):
    today = datetime.date.today()
    monday = today - datetime.timedelta(days=today.weekday())
    event_list = Event.objects.filter(workdate__gte=monday)
    std_list = StdEvent.objects.all()
    context_dict = { 'events': event_list, 'std_events': std_list }
    return render(request, 'weekly/index.html', context_dict)
