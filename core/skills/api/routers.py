from rest_framework.routers import DefaultRouter
from django.urls import path,include

from .views import ViewSetLibrary,ViewSetLanguage

router = DefaultRouter()

router.register(r'language/',ViewSetLibrary,basename='library')
router.register(r'',ViewSetLanguage,basename='language')


urlpatterns = [
    path('',include(router.urls))
]