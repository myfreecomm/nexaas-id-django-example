from django.shortcuts import render
from nexaas_id_client import NexaasIDClient
from nexaas_id_client.support.django.decorators import authorization_required

@authorization_required
def index(request, api_client: NexaasIDClient):
    return render(request, 'id_profile/index.html', {
        'user': api_client.personal_info,
    })
