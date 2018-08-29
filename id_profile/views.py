from django.shortcuts import redirect, render, reverse
from nexaas_id_client import NexaasIDClient
from nexaas_id_client.support.django.decorators import authorization_required
from nexaas_id_client.support.django.helpers import signed_in

@authorization_required
def index(request, api_client: NexaasIDClient):
    res = None
    with signed_in() as unsigned:
        res = render(request, 'id_profile/index.html', {
            'user': api_client.personal_info,
            'widget': api_client.user_widget_url,
        })
    return res or unsigned.redirect
