from django.urls import path,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

import re

urlpatterns = [
    path('signup/', views.register,name='register'),
    path('profile/', views.profile,name='profile'),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

