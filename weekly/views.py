from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from weekly.models import Event, StdEvent
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.contrib.auth.models import User

def index(request):
    today = datetime.date.today()
    monday = today - datetime.timedelta(days=today.weekday())
    event_list = Event.objects.filter(workdate__gte=monday)
    std_list = StdEvent.objects.all()
    users = User.objects.filter(is_superuser__exact=0,is_active__exact=1)
    context_dict = { 'events': event_list, 'std_events': std_list, 'users': users }
    return render(request, 'weekly/index.html', context_dict)
