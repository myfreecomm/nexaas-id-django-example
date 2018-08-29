from django.shortcuts import redirect, render, reverse
from requests.exceptions import HTTPError
from nexaas_id_client import NexaasIDClient
from nexaas_id_client.support.django.decorators import authorization_required

@authorization_required
def index(request, api_client: NexaasIDClient):
    try:
        return render(request, 'id_profile/index.html', {
            'user': api_client.personal_info,
            'widget': api_client.user_widget_url,
        })

    except HTTPError:
        return redirect(reverse('nexaas-id-signout'))
