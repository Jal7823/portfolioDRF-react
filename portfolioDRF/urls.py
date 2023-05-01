from django.contrib import admin
from django.urls import path,include

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    #apps
    path('certifications/',include('core.certifications.api.routers')),
    path('projects/',include('core.projects.api.routers')),
    path('skills/',include('core.skills.api.routers')),


    # YOUR PATTERNS
    path('api/', SpectacularAPIView.as_view(), name='schema'),
    
    # Optional UI:
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
