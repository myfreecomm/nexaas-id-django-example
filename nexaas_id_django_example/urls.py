#from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('oauth/', include('nexaas_id_client.support.django.urls')),
    path('/', include('id_profile.urls')),
    path('', include('id_profile.urls')),
]
