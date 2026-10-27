from django.shortcuts import render


def index(request):
    """
    Entrypoint for the 2D Creative Studio destination.
    """
    context = {
        'destination_name': 'Create — Studio',
        'destination_description': (
            'Interactive 2D Creative Studio workbench for transforming discarded '
            'plastic bottles into creative art, functional items, and eco-sculptures.'
        ),
    }
    return render(request, 'studio/index.html', context)
