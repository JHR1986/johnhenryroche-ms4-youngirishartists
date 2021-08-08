from django.shortcuts import render


# Create your view for Home Page.
def index(request):
    """ View to return the index page """
    return render(request, 'home/index.html')
