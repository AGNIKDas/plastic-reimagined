from django.shortcuts import render


def index(request):
    """
    Entrypoint for the Public Creations Gallery.
    """
    context = {
        'destination_name': 'Gallery — Approved Creations',
        'destination_description': (
            'Public showcase celebrating community upcycling ingenuity. Displays '
            'moderated and approved visitor creations transformed via the 2D Studio.'
        ),
    }
    return render(request, 'gallery/index.html', context)
