from django.shortcuts import render
from django.conf import settings


def index(request):
    """
    Platform entrypoint view presenting the project vision and foundational architecture.
    """
    context = {
        'page_title': 'Plastic Reimagined — Creative Environmental Platform',
        'debug_mode': settings.DEBUG,
        'destinations': [
            {
                'name': 'Create',
                'url_name': 'studio:index',
                'description': '2D Creative Studio for transforming discarded plastic bottles into imaginative designs.',
                'tag': 'Creative Studio',
            },
            {
                'name': 'Discover',
                'url_name': 'catalogue:index',
                'description': 'Environmental discovery catalogue detailing plastic polymer realities, lifecycle, and sustainable alternatives.',
                'tag': 'Discovery Catalogue',
            },
            {
                'name': 'Read',
                'url_name': 'blog:index',
                'description': 'Visual environmental stories, artisan spotlights, and community circularity essays.',
                'tag': 'Environmental Blog',
            },
            {
                'name': 'Gallery',
                'url_name': 'gallery:index',
                'description': 'Public exhibition of approved visitor creations and upcycling breakthroughs.',
                'tag': 'Public Showcase',
            },
        ],
    }
    return render(request, 'core/index.html', context)
