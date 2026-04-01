from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('mainapp.mainurls','mainapp'), namespace="mainapp")),
    path('adparent/', include(('adminapp.adminurls','adminapp'), namespace="adminapp")),
    path('student/', include(('studentapp.stuurls','studentapp'),namespace="studentapp")),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
