from django.shortcuts import render
from .models import Artist


# View for Artists
def all_artists(request):
    """ A view to show all artists """

    artists = Artist.objects.all()

    context = {
        'artists': artists,
    }

    return render(request, 'artists/artists.html', context)
