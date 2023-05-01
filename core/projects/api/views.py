from rest_framework import viewsets,status

from .serializers import SerializersProjects
from ..models import Projects

class ViewSetProjects(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = SerializersProjects