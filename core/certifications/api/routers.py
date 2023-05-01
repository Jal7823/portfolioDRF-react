from rest_framework.routers import DefaultRouter
from django.urls import path,include

from .views import ViewSetCertifications

router = DefaultRouter()

router.register(r'',ViewSetCertifications,basename='certifications')


urlpatterns = [
    path('',include(router.urls))
]