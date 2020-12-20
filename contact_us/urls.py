from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'contact_us'

urlpatterns = [
    path('', views.contact_us, name="contact_us"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
