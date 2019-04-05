from django.urls import path,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

import re
app_name = 'organization'
urlpatterns = [
    path('signup/', views.signup,name='organization_signup'),
	 

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

