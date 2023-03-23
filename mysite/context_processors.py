from .models import Header, Footer, SocialNetworks


def constant(request):
    headers = Header.objects.all()
    footer = Footer.objects.all()
    social_networks = SocialNetworks.objects.all()
    return {
        'headers': headers,
        'footer': footer,
        'social_networks': social_networks
    }
