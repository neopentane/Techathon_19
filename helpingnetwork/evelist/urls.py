from django.urls import path,re_path
from . import views
from organization.models import Organization
from .models import Event
from django.conf import settings
from django.conf.urls.static import static
import re

urlpatterns = [
    path('', views.index,name='index'),
    path('evelist/<int:event_id>/',views.desc,name='desc')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

