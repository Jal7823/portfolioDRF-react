from rest_framework.routers import DefaultRouter
from django.urls import path,include

from .views import ViewSetProjects

router = DefaultRouter()

router.register(r'',ViewSetProjects,basename='projects')


urlpatterns = [
    path('',include(router.urls))
]