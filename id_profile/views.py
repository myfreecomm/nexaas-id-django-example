from django.shortcuts import render
from nexaas_id_client.support.django.decorators import authorization_required

@authorization_required
def index(request, api_client):
    return render(request, 'id_profile/index.html', {
        'user': api_client.personal_info,
        'widget': api_client.user_widget_url,
    })
