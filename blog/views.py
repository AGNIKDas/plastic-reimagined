from django.shortcuts import render


def index(request):
    """
    Entrypoint for the Visual Environmental Blog.
    """
    context = {
        'destination_name': 'Read — Environmental Blog',
        'destination_description': (
            'Visual storytelling, community circular economy reports, and deep '
            'explorations of grassroots upcycling craftsmanship.'
        ),
    }
    return render(request, 'blog/index.html', context)
