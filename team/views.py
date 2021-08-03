from django.shortcuts import render
from .models import Team

# Create your views here.

def all_teams(request):
    """ A view to show all artists """

    teams = Team.objects.all()

    context = {
        'teams': teams,
    }

    return render(request, 'team/teams.html', context)