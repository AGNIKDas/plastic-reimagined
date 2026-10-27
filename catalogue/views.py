from django.shortcuts import render


def index(request):
    """
    Entrypoint for the Environmental Discovery Catalogue.
    """
    context = {
        'destination_name': 'Discover — Environmental Catalogue',
        'destination_description': (
            'Interactive environmental discovery catalogue mapping plastic resin '
            'codes, ocean plastic lifecycle pathways, decomposition timelines, and '
            'sustainable circular alternatives.'
        ),
    }
    return render(request, 'catalogue/index.html', context)
